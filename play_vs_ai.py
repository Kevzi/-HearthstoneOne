import sys
import os
import torch
import random
from typing import Optional

# Path hacks
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.model import HearthstoneModel
from ai.encoder import FeatureEncoder
from ai.mcts import MCTS
from ai.game_wrapper import HearthstoneGame
from ai.actions import Action

def load_latest_model():
    model = HearthstoneModel(FeatureEncoder().input_dim, 260) # 260 is hardcoded ACTION_SPACE_SIZE
    
    if not os.path.exists("models"):
        print("No models found! Please train first.")
        return None
        
    checkpoints = [f for f in os.listdir("models") if f.startswith("checkpoint_iter_") and f.endswith(".pt")]
    if not checkpoints:
        print("No checkpoints found! Please train first.")
        return None
        
    # Sort to find latest
    checkpoints.sort(key=lambda x: int(x.split('_')[-1].replace('.pt', '')))
    latest = checkpoints[-1]
    path = os.path.join("models", latest)
    
    # Load on CPU for playing
    checkpoint = torch.load(path, map_location="cpu")
    if 'model_state_dict' in checkpoint:
        model.load_state_dict(checkpoint['model_state_dict'])
    else:
        model.load_state_dict(checkpoint)
        
    model.eval()
    print(f"Loaded AI Brain: {latest}")
    return model

def print_game_state(env):
    game = env.game
    p1 = game.players[0] # Human
    p2 = game.players[1] # AI
    
    # Simple ASCII rendering
    print("\n" + "="*60)
    print(f"OPPONENT (AI) - HP: {p2.hero.health}/{p2.hero.max_health} | Mana: {p2.mana}/{p2.max_mana}")
    print(f"Hand: {len(p2.hand)} cards | Deck: {len(p2.deck)}")
    print("Minions:")
    for i, m in enumerate(p2.board):
        print(f"  [{i}] {m.name} ({m.attack}/{m.health}) {m.get_status_str()}")
        
    print("-" * 60)
    print("Minions:")
    for i, m in enumerate(p1.board):
        print(f"  [{i}] {m.name} ({m.attack}/{m.health}) {m.get_status_str()}")
        
    print(f"YOU (Human) - HP: {p1.hero.health}/{p1.hero.max_health} | Mana: {p1.mana}/{p1.max_mana}")
    print("Hand:")
    for i, c in enumerate(p1.hand):
        print(f"  [{i}] {c.name} ({c.cost} mana) - {c.description[:50]}...")
    print("="*60 + "\n")

def get_human_action(game, legal_indices):
    while True:
        try:
            print("Actions: 'play <i> [target]', 'attack <i> <target>', 'hero', 'end'")
            cmd = input("Your Move > ").strip().lower().split()
            if not cmd: continue
            
            action = None
            
            if cmd[0] == "end":
                action = Action(type="END_TURN")
                
            elif cmd[0] == "play" and len(cmd) >= 2:
                card_idx = int(cmd[1])
                target_idx = int(cmd[2]) if len(cmd) > 2 else 0
                action = Action(type="PLAY_CARD", index=card_idx, target=target_idx)
                
            elif cmd[0] == "attack" and len(cmd) >= 3:
                attacker_idx = int(cmd[1])
                target_idx = int(cmd[2])
                action = Action(type="ATTACK", index=attacker_idx, target=target_idx)
                
            elif cmd[0] == "hero":
                target_idx = int(cmd[1]) if len(cmd) > 1 else 0
                action = Action(type="HERO_POWER", target=target_idx)
            
            if action:
                # Check match with legal_actions if you want strict validation here
                # But for now let the engine handle illegal moves, or we just trust input
                return action
            else:
                print("Invalid command format.")
                
        except ValueError:
            print("Invalid numbers.")
        except Exception as e:
            print(f"Error parse: {e}")

def play_vs_ai():
    ai_model = load_latest_model()
    if not ai_model: return
    
    encoder = FeatureEncoder()
    env = HearthstoneGame()
    env.reset() # Standard reset
    
    # Force human to be Player 1 for now
    human_player = env.game.players[0]
    ai_player = env.game.players[1]
    
    print("Game Started! You are Player 1.")
    
    # --- DECK SELECTION ---
    from simulator.deck_generator import DeckGenerator
    available_decks = DeckGenerator._load_meta_decks()
    
    print("\nSelect your Deck:")
    if not available_decks:
        print("No Meta Decks found in data/meta_decks.json. Using Random Deck.")
        player_deck, player_class, player_sb = None, None, {}
    else:
        for i, (cls, name, _) in enumerate(available_decks):
            print(f"[{i}] {cls} - {name}")
        print("[R] Random Meta Deck")
        
        choice = input(f"Choose Deck ID [0-{len(available_decks)-1}] or 'R': ").strip().upper()
        if choice == 'R':
             player_class, player_deck, _, player_sb = DeckGenerator.get_random_meta_deck()
        else:
            try:
                idx = int(choice)
                if 0 <= idx < len(available_decks):
                    cls, name, data = available_decks[idx]
                    player_class = cls
                    # Decode data if needed
                    if isinstance(data, str):
                        decoded = DeckGenerator.decode_deck_string(data)
                        player_deck = decoded["cards"]
                        player_sb = decoded["sideboards"]
                    else:
                        player_deck = data
                        player_sb = {} # Not supported for direct list yet
                    print(f"Selected: {name}")
                else:
                    print("Invalid index. Using Random.")
                    player_class, player_deck, _, player_sb = DeckGenerator.get_random_meta_deck()
            except:
                 print("Invalid input. Using Random.")
                 player_class, player_deck, _, player_sb = DeckGenerator.get_random_meta_deck()

    # AI uses Random Meta Deck for challenge
    ai_class, ai_deck, ai_deck_name, ai_sb = DeckGenerator.get_random_meta_deck()
    print(f"\nOpponent (AI) selected: {ai_class} - {ai_deck_name}")
    
    # Initialize Game with chosen decks
    # We need to manually inject them into reset() but HearthstoneGame.reset takes IDs
    # and handles sideboards? Wait, reset() implementation in game_wrapper.py handles sideboards 
    # BUT only if we pass None. If we pass deck lists, we lose sideboards currently.
    # Let's verify reset() signature in game_wrapper.py.
    # It does NOT take sideboards as args. It generates them if deck is None.
    # We should probably update game_wrapper.py later to accept sideboards,
    # but for now let's just pass the deck lists. Sideboards (Zilliax) might be missing for Human.
    
    # HACK: Manually set sideboards after reset if needed, or just let it be for now.
    # The current reset() accepts deck1 (list of IDs).
    
    env.reset(deck1=player_deck, deck2=ai_deck, class1=player_class, class2=ai_class)
    
    # Inject sideboard manualy for Player 1 if possible
    # env.game.players[0].sideboard = player_sb
    if player_sb:
        env.game.players[0].sideboard = player_sb
        
    if ai_sb:
        env.game.players[1].sideboard = ai_sb
        
    # --- END DECK SELECTION ---
    
    while not env.is_game_over:
        current_turn_player = env.current_player
        
        if current_turn_player == human_player:
            print_game_state(env)
            # Human turn
            # In a real CLI we would filter legal actions. 
            # For this quick demo, we ask user to type.
            action = get_human_action(env.game, [])
            
            # Application
            # Note: We need to map Action object back to the engine's apply
            try:
                # We need to translate our Action object -> Engine logic
                # The engine 'step' method usually takes an index or Action object
                # depending on implementation.
                # Let's assume env.step() handles Action objects mostly.
                env.step(action) 
            except Exception as e:
                print(f"Action failed (Illegal?): {e}")
            
        else:
            # AI Turn
            print("AI is thinking...", end="", flush=True)
            # Use MCTS or Raw network policy? MCTS is stronger.
            root_game_state = env.game.clone()
            mcts = MCTS(ai_model, encoder, root_game_state, num_simulations=50)
            mcts_probs = mcts.search(root_game_state)
            
            # Greedy pick
            import numpy as np
            best_action_idx = np.argmax(mcts_probs)
            action = Action.from_index(best_action_idx)
            
            print(f" Done! AI plays: {action}")
            env.step(action)
            
    if env.game.winner == human_player:
        print("\nVICTORY! You defeated the DeepMind AI!")
    else:
        print("\nDEFEAT! The machine is superior.")

if __name__ == "__main__":
    play_vs_ai()
