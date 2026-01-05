"""Effect for Nerubian Swarmguard (CORE_RLK_062).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Summon two
copies of this minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass