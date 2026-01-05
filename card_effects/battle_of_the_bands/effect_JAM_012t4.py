"""Effect for Karaoke Totemcarver (JAM_012t4).

Card Text: [x]<b>Battlecry:</b> Summon a
0/4 Jukebox Totem.
<i>(Changes each turn.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass