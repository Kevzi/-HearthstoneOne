"""Effect for SC_762 (Mothership) in SPACE"""

def battlecry(game, source, target):
    """Battlecry: Get two random Protoss minions."""
    import random
    from simulator.card_loader import CardDatabase
    
    protoss_ids = [c.card_id for c in CardDatabase.get_collectible_cards() 
                   if c.card_set == "SPACE" and c.card_type.name == "MINION" 
                   and "MECHANICAL" in (c.races or [])]
    
    for _ in range(2):
        if protoss_ids:
            card_id = random.choice(protoss_ids)
            source.controller.add_to_hand(create_card(card_id, source.controller))

def deathrattle(game, source):
    """Deathrattle: Get two random Protoss minions."""
    import random
    from simulator.card_loader import CardDatabase
    
    protoss_ids = [c.card_id for c in CardDatabase.get_collectible_cards() 
                   if c.card_set == "SPACE" and c.card_type.name == "MINION"
                   and "MECHANICAL" in (c.races or [])]
    
    for _ in range(2):
        if protoss_ids:
            card_id = random.choice(protoss_ids)
            source.controller.add_to_hand(create_card(card_id, source.controller))
