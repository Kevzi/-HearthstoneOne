import random
from typing import List, Dict, Optional, Tuple
from .card_loader import CardDatabase, CardClass, CardType

class DeckGenerator:
    """Handles parsing deck codes and generation."""
    
    _dbf_map: Dict[int, str] = {}
    _cached_meta_decks = {}

    @staticmethod
    def _load_meta_decks():
        """Load decks from data/meta_decks.json.
        
        Supports two formats:
        - "code": deckstring to decode
        - "cards": direct list of card IDs
        """
        import json
        import os
        
        json_path = os.path.join(os.path.dirname(__file__), "..", "data", "meta_decks.json")
        json_path = os.path.abspath(json_path)
        
        # Returns list of (class_name, deck_name, deck_data) where deck_data is either a code or a card list
        decks_list = []
        
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for class_name, decks in data.items():
                    for deck in decks:
                        if 'cards' in deck:
                            # Direct card IDs format
                            decks_list.append((class_name, deck['name'], deck['cards']))
                        elif 'code' in deck:
                            # Deckstring format
                            decks_list.append((class_name, deck['name'], deck['code']))
            except Exception as e:
                print(f"Error loading meta_decks.json: {e}")
        
        return decks_list

    @staticmethod
    def get_meta_decks_for_class(player_class: str) -> List[List[str]]:
        """Get all meta decks for a specific class."""
        decks_list = DeckGenerator._load_meta_decks()
        relevant_decks = []
        for cls, name, deck_data in decks_list:
            if cls.upper() == player_class.upper():
                if isinstance(deck_data, list):
                    # Direct card IDs
                    if len(deck_data) >= 20:
                        relevant_decks.append(deck_data)
                else:
                    # Deckstring
                    decoded = DeckGenerator.decode_deck_string(deck_data)
                    if decoded and len(decoded) >= 20:
                        relevant_decks.append(decoded)
        return relevant_decks

    @staticmethod
    def get_preset_deck(archetype: str) -> List[str]:
        """Get a predefined iconic deck by archetype name."""
        decks_list = DeckGenerator._load_meta_decks()
        for class_name, name, deck_data in decks_list:
            if archetype.lower() in name.lower():
                if isinstance(deck_data, list):
                    # Direct card IDs
                    return deck_data
                else:
                    # Deckstring
                    decoded = DeckGenerator.decode_deck_string(deck_data)
                    if decoded:
                        return decoded
        return DeckGenerator.get_random_deck()

    @staticmethod
    def get_random_meta_deck() -> Tuple[str, List[str], str]:
        """Get a random meta deck. Returns (class_name, card_ids, deck_name)."""
        decks_list = DeckGenerator._load_meta_decks()
        if not decks_list:
            # Fallback
            cls = "MAGE"
            return cls, DeckGenerator.get_random_deck(cls), "Random Mage"
            
        import random
        class_name, deck_name, deck_data = random.choice(decks_list)
        
        # Check format
        if isinstance(deck_data, list):
            # Direct card IDs format
            card_ids = deck_data
        else:
            # Deckstring format - decode it
            card_ids = DeckGenerator.decode_deck_string(deck_data)
        
        # Ensure 30 cards
        if card_ids and len(card_ids) > 0:
             # Safety pad if partial
             while len(card_ids) < 30:
                 card_ids.append(card_ids[0])
             return class_name, card_ids[:30], deck_name
        
        return class_name, DeckGenerator.get_random_deck(class_name), f"Random {class_name}"

    @staticmethod
    def decode_deck_string(deck_string: str) -> Optional[List[str]]:
        """Decode a Hearthstone deck string to list of card IDs."""
        try:
            from hearthstone.deckstrings import parse_deckstring
            if not DeckGenerator._dbf_map:
                DeckGenerator._build_dbf_map()
                
            decoded = parse_deckstring(deck_string)
            cards = decoded[0]
            result = []
            for dbf_id, count in cards:
                # Filter out corrupted sideboard entries:
                # - count > 2 is impossible in a normal deck (max 2 copies, 1 for legendary)
                # - dbf_id < 100 are placeholders/delimiters, not real cards
                if count > 2 or dbf_id < 100:
                    continue
                    
                card_id = DeckGenerator._dbf_map.get(dbf_id)
                if card_id:
                    result.extend([card_id] * count)
                else:
                    result.extend([f"DBF:{dbf_id}"] * count)
            return result
        except Exception as e:
            print(f"Deck decoding error: {e}")
            return None

    @staticmethod
    def _build_dbf_map():
        """Build the DBF ID to Card ID map."""
        db = CardDatabase.get_instance()
        if not db._loaded:
            db.load()
        for card in db._cards.values():
            if hasattr(card, 'dbf_id') and card.dbf_id:
                DeckGenerator._dbf_map[card.dbf_id] = card.card_id

    @staticmethod
    def get_random_deck(player_class: str = "MAGE", size: int = 30) -> List[str]:
        """Generate a random valid deck for a class."""
        db = CardDatabase.get_instance()
        if not db._loaded: db.load()
            
        valid_cards = []
        for card in db._cards.values():
            if not card.collectible or card.card_type == CardType.HERO: continue
            is_class = str(card.card_class).upper() == player_class.upper()
            is_neutral = str(card.card_class).upper() == "NEUTRAL" or "NEUTRAL" in str(card.card_class).upper()
            
            if is_class or is_neutral:
                valid_cards.append(card.card_id)
        
        if not valid_cards:
            valid_cards = [c.card_id for c in db._cards.values() if c.collectible and c.card_type != CardType.HERO]
            
        return random.choices(valid_cards, k=size) if valid_cards else []
