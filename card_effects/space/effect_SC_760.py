"""SC_760 - Resonance Coil: Deal 5 damage to a minion. Get a random Protoss spell."""

def on_play(game, player, card, target=None):
    # Deal 5 damage to target minion
    if target and hasattr(target, 'take_damage'):
        target.take_damage(5, card)
    
    # Get a random Protoss spell
    import random
    from simulator.card_loader import CardDatabase
    
    db = CardDatabase.get_instance()
    protoss_spells = [c for c in db._cards.values() 
                      if c.card_set == 'SPACE' 
                      and c.card_type.name == 'SPELL'
                      and 'SC_' in c.card_id]
    
    if protoss_spells:
        chosen = random.choice(protoss_spells)
        from simulator.factory import create_card
        new_card = create_card(chosen.card_id, game)
        if new_card:
            player.add_to_hand(new_card)
