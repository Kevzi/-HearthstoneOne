"""Effect for Troubled Mechanic (GDB_463).

Card Text: [x]<b>Divine Shield</b>
<b><b>Spellburst</b>:</b> Draw a Draenei.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)