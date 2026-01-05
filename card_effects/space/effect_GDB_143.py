"""Effect for Nexus-Prince Shaffar (GDB_143).

Card Text: [x]<b>Spellburst:</b> Give a minion
in your hand +3/+3 and this
<b>Spellburst</b> <i>(unless it already
has these effects).</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Effect: [x]<b>Spellburst:</b> Give a minion
in your hand +3/+3 and this
<b>Spellburst</b> <i>(unless it already
has these effects).</i>
    # TODO: Implement
    pass