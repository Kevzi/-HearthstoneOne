"""Effect for Distress Signal (GDB_883).

Card Text: [x]Summon two random
2-Cost minions.
Refresh 2 Mana Crystals.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass