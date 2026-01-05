"""Effect for Dirty Rat (CORE_CFM_790).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Your opponent
summons a random minion
from their hand.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass