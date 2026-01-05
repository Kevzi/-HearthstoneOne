"""Effect for Astrobiologist (GDB_874).

Card Text: <b>Battlecry:</b> At the start
of your next turn,
<b>Discover</b> a spell.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass