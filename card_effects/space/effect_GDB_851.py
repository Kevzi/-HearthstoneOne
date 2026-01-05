"""Effect for Astral Phaser (GDB_851).

Card Text: <b>Choose One -</b> Deal $2 damage to two random enemy minions; or Make one <b>Dormant</b> for 2 turns.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)