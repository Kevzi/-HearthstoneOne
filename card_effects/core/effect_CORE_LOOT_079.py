"""CORE_LOOT_079 - Wandering Monster: When hero attacked, summon a 3-Cost minion as new target."""

def on_hero_attacked(game, owner, secret, attacker=None, defender=None):
    if defender and defender == owner.hero and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        from simulator.card_loader import CardDatabase
        import random
        
        # Find a random 3-cost minion
        db = CardDatabase.get_instance()
        three_cost = [c for c in db._cards.values() 
                      if c.cost == 3 and c.card_type.name == 'MINION' and c.collectible]
        
        if three_cost:
            chosen = random.choice(three_cost)
            card = create_card(chosen.card_id, game)
            if card:
                m = Minion(card.data, game)
                m.controller = owner
                owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
