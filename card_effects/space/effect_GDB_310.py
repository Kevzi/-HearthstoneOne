"""Effect for Ethereal Oracle (GDB_310).

Card Text: <b>Spell Damage +1</b>
<b><b>Spellburst</b>:</b> Draw 2 spells.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)