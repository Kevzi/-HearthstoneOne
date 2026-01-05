"""Effect for Firelands Portal (CORE_KAR_076).

Card Text: Deal $6 damage. Summon a random
6-Cost minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 6, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass