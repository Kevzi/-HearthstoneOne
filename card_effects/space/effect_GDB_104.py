"""Effect for Felfire Thrusters (GDB_104).

Card Text: [x]<b><b>Spellburst</b>:</b> Deal this
minion's Attack damage to
2 random enemy minions.
<b>Starship Piece</b>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)