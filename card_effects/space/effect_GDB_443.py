"""Effect for Cosmonaut (GDB_443).

Card Text: <b>Battlecry:</b> <b>Discover</b> a spell from your deck. Reduce its Cost by (5).
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass