"""Effect for Spontaneous Combustion (GDB_456).

Card Text: Deal $4 damage to a random enemy. If you played an Elemental last turn, choose the target.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 4 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 4, source)