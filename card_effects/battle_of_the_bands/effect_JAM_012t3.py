"""Effect for Blazing Totemcarver (JAM_012t3).

Card Text: [x]<b>Battlecry:</b> Summon a
0/3 Flametongue Totem.
<i>(Changes each turn.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass