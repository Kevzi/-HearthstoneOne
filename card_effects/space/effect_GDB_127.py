"""Effect for K'ara, the Dark Star (GDB_127).

Card Text: [x]<b><b>Spellburst</b>:</b> Steal 2 Health
from a random enemy.
<i>(Shadow spells don't remove
this <b>Spellburst</b>.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)