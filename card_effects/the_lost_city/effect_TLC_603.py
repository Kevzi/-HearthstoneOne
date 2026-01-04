"""TLC_603 - Platysaur"""

def on_battlecry(game, player, card, target=None):
    player.draw()

def on_deathrattle(game, minion):
    owner = minion.controller
    # Discard a card (randomly usually)
    if owner.hand:
        import random
        to_discard = random.choice(owner.hand)
        owner.discard(to_discard)
