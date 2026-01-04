import sys
import os
import torch
import numpy as np
import time
from typing import List, Tuple, Optional, Dict
from concurrent.futures import ProcessPoolExecutor, as_completed

# Path hacks (assuming run from root)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.model import HearthstoneModel
from ai.encoder import FeatureEncoder
from ai.mcts import MCTS
from ai.game_wrapper import HearthstoneGame
from ai.replay_buffer import ReplayBuffer
from ai.actions import Action

def _play_game_worker(model_state, input_dim, action_dim, mcts_sims, game_idx, verbose):
    """Worker function for multiprocessing."""
    try:
        # Crucial for Windows: limit torch threads per process to save RAM
        torch.set_num_threads(1)
        
        # Load card database ONCE per worker process
        from simulator import CardDatabase
        db = CardDatabase.get_instance()
        if not db.is_loaded:
            import contextlib
            import io
            with contextlib.redirect_stdout(io.StringIO()):
                db.load()
        
        # Each process needs its own model and encoder instance
        model = HearthstoneModel(input_dim, action_dim)
        model.load_state_dict(model_state)
        model.eval()
        encoder = FeatureEncoder()
        
        # Randomize perspective: sometimes the AI is Player 1, sometimes Player 2
        perspective = 1 if np.random.random() > 0.5 else 2
        
        env = HearthstoneGame(perspective=perspective)
        env.reset()
        
        trajectory = []
        step_count = 0
        max_steps = 500
        # Prepare state for MCTS (reuse encoder)
        while not env.is_game_over and step_count < max_steps:
            # We must clone for MCTS as it explores future branches
            root_game_state = env.game.clone()
            
            # MCTS initialization is now lighter with the fix in ai/mcts.py
            mcts = MCTS(model, encoder, root_game_state, num_simulations=mcts_sims)
            mcts_probs = mcts.search(root_game_state)
            
            # Current player perspective encoding
            encoded_state = encoder.encode(env.get_state())
            current_p_id = 1 if env.current_player == env.game.players[0] else 2
            
            # Store transition (State, Probs, CurrentPlayerID)
            trajectory.append((encoded_state, mcts_probs, current_p_id))
            
            # Pick action using MCTS probabilities
            action_idx = np.random.choice(len(mcts_probs), p=mcts_probs)
            
            # Execute action using simulator's internal action if possible for speed
            # Find the Action object from MCTS results to reuse its simulation metadata
            action = Action.from_index(action_idx)
            env.step(action)
                
            step_count += 1
            
        # Determine winner
        winner = 0
        if env.game.winner:
            winner = 1 if env.game.winner == env.game.players[0] else 2
        elif step_count >= max_steps:
            if verbose: print(f"Game {game_idx} timed out after {max_steps} steps.")
            
        return trajectory, winner

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

class DataCollector:
    def __init__(self, model: HearthstoneModel, buffer: ReplayBuffer, num_workers: int = 4):
        self.model = model
        self.buffer = buffer
        self.encoder = FeatureEncoder()
        self.num_workers = num_workers
        
    def collect_games(self, num_games: int, mcts_sims: int = 25, verbose: bool = False):
        """Run self-play games using multiprocessing."""
        
        # CRITICAL FIX: Buffer was poisoned by biased P1-only games and P2 random moves.
        # Clearing once to ensure new training is healthy.
        if len(self.buffer) > 0 and not hasattr(self, '_buffer_flushed'):
            print("Cleaning biased replay buffer to restart with healthy symmetric data (P1/P2 random perspective)...")
            self.buffer.clear()
            self._buffer_flushed = True

        print(f"Starting parallel selection of {num_games} games...")
        
        start_time = time.time()
        winners = {0: 0, 1: 0, 2: 0}
        
        # Pull model state to pass to workers on CPU
        cpu_model_state = {k: v.cpu() for k, v in self.model.state_dict().items()}
        
        completed_games = 0
        
        if self.num_workers == 0:
            # Sequential execution for debugging/stability
            for i in range(num_games):
                try:
                    trajectory, winner = _play_game_worker(
                        cpu_model_state,
                        self.model.input_dim,
                        self.model.action_dim,
                        mcts_sims,
                        i,
                        verbose
                    )
                    self.buffer.add_game(trajectory, winner)
                    winners[winner] = winners.get(winner, 0) + 1
                    
                    completed_games += 1
                    elapsed = time.time() - start_time
                    avg_time = elapsed / completed_games if completed_games > 0 else 0
                    
                    winner_str = f"Player {winner}" if winner > 0 else "Draw/Timeout"
                    print(f"[{completed_games}/{num_games}] Game completed. Winner: {winner_str}. Buffer: {len(self.buffer)}. Avg: {avg_time:.2f}s/game")
                except Exception as e:
                    print(f"Sequential game failed: {e}")
                    
        else:
            # Parallel execution
            with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
                futures = []
                for i in range(num_games):
                    futures.append(executor.submit(
                        _play_game_worker, 
                        cpu_model_state,
                        self.model.input_dim,
                        self.model.action_dim,
                        mcts_sims,
                        i,
                        verbose
                    ))
            
            for future in as_completed(futures):
                try:
                    trajectory, winner = future.result()
                    self.buffer.add_game(trajectory, winner)
                    winners[winner] = winners.get(winner, 0) + 1
                    
                    completed_games += 1
                    elapsed = time.time() - start_time
                    avg_time = elapsed / completed_games
                    
                    winner_str = f"Player {winner}" if winner > 0 else "Draw/Timeout"
                    print(f"[{completed_games}/{num_games}] Game completed. Winner: {winner_str}. Buffer: {len(self.buffer)}. Avg: {avg_time:.2f}s/game")
                except Exception as e:
                    print(f"Game worker failed: {e}")
                    
        return winners
