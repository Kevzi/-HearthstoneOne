"""
Log Parser for Hearthstone Power.log.
Converts raw log lines into Game State updates for the Simulator.
"""

import re
from typing import Optional, Dict, List
from simulator.game import Game
from simulator.player import Player
from simulator.card_loader import CardDatabase

class LogParser:
    def __init__(self, game: Game):
        self.game = game
        self.entity_map: Dict[int, object] = {} # ID -> Entity (Player/Card/Hero)
        
        # Regex for TAG_CHANGE
        # Example: TAG_CHANGE Entity=[id=1 cardId=GAME_005 name=Coin] tag=ZONE value=HAND
        # Example: TAG_CHANGE Entity=Kevin tag=CURRENT_PLAYER value=1
        self.regex_tag = re.compile(r"TAG_CHANGE Entity=(.*?) tag=(.*?) value=(.*)")
        
        # Regex for Entity parsing from the [...] block
        # [id=1 cardId=GAME_005 name=Coin]
        self.regex_entity_block = re.compile(r"\[id=(\d+)(?: cardId=(.*?))?(?: name=(.*?))?\]")
        
    def parse_line(self, line: str):
        """Process a single log line."""
        line = line.strip()
        
        # We only care about PowerTaskList.DebugPrintPower logs generally
        if "DebugPrintPower" not in line and "PowerTaskList" not in line:
            return

        # 1. TAG_CHANGE (Most updates happen here)
        tag_match = self.regex_tag.search(line)
        if tag_match:
            entity_str = tag_match.group(1)
            tag = tag_match.group(2)
            value = tag_match.group(3)
            self._handle_tag_change(entity_str, tag, value)
            return

        # 2. BLOCK_START (Actions like Play Card, Attack)
        if "BLOCK_START" in line:
            # TODO: Handle blocks to group actions
            pass

    def _handle_tag_change(self, entity_str: str, tag: str, value: str):
        """Update game state based on tag change."""
        
        # Resolve Entity ID
        entity_id = self._resolve_entity_id(entity_str)
        if entity_id is None:
            return

        # Handle Specific Tags
        if tag == "ZONE":
            self._handle_zone_change(entity_id, value)
        elif tag == "CURRENT_PLAYER":
            if value == "1":
                # Find player with this ID and set as current
                pass
        # ... add more tags (DAMAGE, HEALTH, ATK, etc.)

    def _resolve_entity_id(self, entity_str: str) -> Optional[int]:
        """Parses entity string to get ID."""
        # Case 1: [id=123 ...]
        block_match = self.regex_entity_block.search(entity_str)
        if block_match:
            return int(block_match.group(1))
            
        # Case 2: Name (e.g. "Kevin") - usually refers to Player
        # We need to map names to IDs if possible, or use pre-registered players
        # For valid simulation, we need correct IDs.
        # Hearthstone logs usually use names for Players in TAG_CHANGE.
        if entity_str == "GameEntity":
            return 1 # Usually GameEntity is 1
            
        # Try to find player by name
        for p in self.game.players:
            if p.name == entity_str:
                # Return player entity ID? Or map player object?
                # Simulator players don't explicitly carry the Log ID.
                # We might need to map them.
                return None # TODO: Player ID mapping

        return None
        
    def _handle_zone_change(self, entity_id: int, zone_value: str):
        """Moves card between zones (Deck -> Hand -> Play)."""
        # This is where we create card instances in the simulator!
        pass
