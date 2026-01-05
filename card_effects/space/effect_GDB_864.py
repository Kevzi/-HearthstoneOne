"""Effect for First Contact (GDB_864).

Card Text: Summon two random 1-Cost minions. <b>Overload:</b> (1)
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass