"""Effect for Bubba (VAC_464t6).

Card Text: [x]<b>Battlecry</b>: Summon six
1/1 Bloodhounds with
<b>Rush</b> to attack an
enemy minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass