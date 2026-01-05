"""Effect for Murloc Growfin (MIS_307t1).

Card Text: [x]<b>Gigantic</b>
<b>Battlecry:</b> Summon a
Tinyfin with <b>Rush</b> and stats
equal to this minion's.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass