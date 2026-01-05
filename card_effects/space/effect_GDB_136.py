"""Effect for Exarch Hataaru (GDB_136).

Card Text: <b>Battlecry:</b> <b>Discover</b> a spell and reduce its Cost by (1).
If you play it this turn, repeat this effect.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass