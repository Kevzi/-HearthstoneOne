"""Effect for Siege Tank, Deployed (SC_413t).

Card Text: <b>Battlecry:</b> Deal 10 damage to a random enemy minion. Excess damage hits the enemy hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 10 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 10, source)