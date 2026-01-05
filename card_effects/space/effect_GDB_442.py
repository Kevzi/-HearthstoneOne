"""Effect for K'ure, the Light Beyond (GDB_442).

Card Text: [x]<b><b>Spellburst</b>:</b> Summon a
random 3-Cost minion.
<i>(Holy spells don't remove
this <b>Spellburst</b>.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass