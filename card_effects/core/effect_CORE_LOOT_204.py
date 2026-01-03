"""CORE_LOOT_204 - Cheat Death: When a friendly minion dies, return it to hand. Costs (2) less."""

def on_friendly_death(game, owner, secret, minion=None):
    if minion and minion.controller == owner and len(owner.hand) < 10:
        from simulator.factory import create_card
        
        # Create a copy in hand with reduced cost
        copy = create_card(minion.card_id, game)
        if copy:
            copy.cost = max(0, copy.cost - 2)
            owner.add_to_hand(copy)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
