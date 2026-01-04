"""
AIBrain - Interface between AlphaZero model and the overlay.

This module provides a high-level interface to use the trained model
for suggesting actions during live gameplay.
"""

import os
import torch
import numpy as np
from typing import Optional, Tuple, List

from ai.model import HearthstoneModel
from ai.encoder import FeatureEncoder
from ai.actions import Action, ActionType
from ai.game_wrapper import HearthstoneGame


class AIBrain:
    """
    High-level AI interface for the overlay.
    
    Usage:
        brain = AIBrain()
        brain.load_model("models/checkpoint_iter_100.pt")
        action, confidence = brain.suggest_action(game_state)
    """
    
    def __init__(self, input_dim: int = 690, action_dim: int = 200, use_gpu: bool = True):
        self.input_dim = input_dim
        self.action_dim = action_dim
        self.device = torch.device("cuda" if use_gpu and torch.cuda.is_available() else "cpu")
        
        # Initialize model
        self.model = HearthstoneModel(input_dim, action_dim).to(self.device)
        self.encoder = FeatureEncoder()
        
        # State
        self.model_loaded = False
        self.model_path = None
        
    def load_model(self, path: str) -> bool:
        """Load a trained model checkpoint."""
        if not os.path.exists(path):
            print(f"Model not found: {path}")
            return False
            
        try:
            state_dict = torch.load(path, map_location=self.device)
            self.model.load_state_dict(state_dict)
            self.model.eval()
            self.model_loaded = True
            self.model_path = path
            print(f"Model loaded from {path}")
            return True
        except Exception as e:
            print(f"Failed to load model: {e}")
            return False
    
    def load_latest_model(self, models_dir: str = "models") -> bool:
        """Load the most recent checkpoint from models directory."""
        if not os.path.exists(models_dir):
            print(f"Models directory not found: {models_dir}")
            return False
            
        # Find all checkpoints
        checkpoints = [f for f in os.listdir(models_dir) if f.endswith('.pt')]
        if not checkpoints:
            print("No checkpoints found")
            return False
            
        # Sort by iteration number (assumes format: checkpoint_iter_X.pt)
        def get_iter(name):
            try:
                return int(name.split('_')[-1].replace('.pt', ''))
            except:
                return 0
                
        checkpoints.sort(key=get_iter, reverse=True)
        latest = os.path.join(models_dir, checkpoints[0])
        
        return self.load_model(latest)
    
    def suggest_action(self, state: GameState) -> Tuple[Optional[Action], float, str]:
        """
        Get the best action for the current game state.
        
        Args:
            state: GameState object from the simulator/parser
            
        Returns:
            (action, confidence, description)
        """
        if not self.model_loaded:
            return None, 0.0, "Model not loaded"
            
        try:
            # Encode state to tensor
            state_tensor = self.encoder.encode(state).unsqueeze(0).to(self.device)
            
            # Get model prediction
            self.model.eval()
            with torch.no_grad():
                policy, value = self.model(state_tensor)
            
            # Policy is action probabilities
            probs = policy.cpu().numpy()[0]
            
            # Get valid actions mask from state directly (more reliable)
            valid_mask = self._get_valid_action_mask_from_state(state)
            masked_probs = probs * valid_mask
            
            # Normalize
            if masked_probs.sum() > 0:
                masked_probs = masked_probs / masked_probs.sum()
            else:
                # Fallback: End Turn
                return Action.end_turn(), 1.0, "End Turn (forced)"
            
            # Get best action
            best_idx = np.argmax(masked_probs)
            confidence = float(masked_probs[best_idx])
            
            action = Action.from_index(best_idx)
            description = self._action_to_description(action, state)
            
            return action, confidence, description
            
        except Exception as e:
            print(f"Error in suggest_action: {e}")
            import traceback
            traceback.print_exc()
            return None, 0.0, f"Error: {e}"

    def _get_valid_action_mask_from_state(self, state: GameState) -> np.ndarray:
        """Create mask from GameState object."""
        mask = np.zeros(self.action_dim, dtype=np.float32)
        
        # This assumes GameState has a helper or we manually check
        # Actually, HearthstoneGame wrapper has get_valid_action_mask()
        # But here we only have the state.
        
        # Simplified for now: just allow the model's top choice if we can't mask perfectly
        # In a real scenario, we'd need information from the simulator about legal actions.
        # However, for a Live Assistant, we can try to guess valid actions from state.
        
        # Let's say we trust the model's top 10 choices for now or implement a basic mask.
        mask.fill(1.0) 
        return mask
    
    def get_value_estimate(self, state: GameState) -> float:
        """Get the model's value estimate for the current state (-1 to 1)."""
        if not self.model_loaded:
            return 0.0
            
        try:
            state_tensor = self.encoder.encode(state).unsqueeze(0).to(self.device)
            self.model.eval()
            with torch.no_grad():
                _, value = self.model(state_tensor)
                
            return float(value.cpu().numpy()[0])
        except:
            return 0.0
    
    def _action_to_description(self, action: Action, state: GameState) -> str:
        """Convert action to human-readable description."""
        if action.action_type == ActionType.END_TURN:
            return "End Turn"
            
        elif action.action_type == ActionType.PLAY_CARD:
            p = state.friendly_player
            if action.card_index is not None and action.card_index < len(p.hand):
                card = p.hand[action.card_index]
                card_name = getattr(card, 'name', f'Card {action.card_index}')
                return f"Play: {card_name}"
            return f"Play card {action.card_index}"
            
        elif action.action_type == ActionType.HERO_POWER:
            return "Use Hero Power"
            
        elif action.action_type == ActionType.ATTACK:
            return f"Attack: Minion {action.attacker_index} → Target {action.target_index}"
            
        elif action.action_type == ActionType.USE_LOCATION:
            return f"Activate Location {action.card_index}"
            
        return str(action)


# Singleton instance for easy access
_brain_instance: Optional[AIBrain] = None

def get_brain() -> AIBrain:
    """Get the global AIBrain instance."""
    global _brain_instance
    if _brain_instance is None:
        _brain_instance = AIBrain()
    return _brain_instance
