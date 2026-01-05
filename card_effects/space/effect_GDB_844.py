"""Effect for Detailed Notes (GDB_844).

Card Text: <b>Discover</b> a Beast that costs (5) or more. Reduce its Cost by (2).
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass