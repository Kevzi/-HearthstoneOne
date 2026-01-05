"""Effect for Loud Totemcarver (JAM_012t).

Card Text: [x]<b>Battlecry:</b> Summon a
0/3 Stereo Totem.
<i>(Changes each turn.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass