"""Effect for Parallax Cannon (GDB_843).

Card Text: [x]Has +2 Attack if you've
<b><b>Discover</b>ed</b> this turn.
<b><b>Spellburst</b>:</b> Your hero is
<b>Immune</b> this turn.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass