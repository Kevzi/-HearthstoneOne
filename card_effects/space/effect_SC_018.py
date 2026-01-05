"""Effect for Viper (SC_018).

Card Text: [x]<b>Battlecry:</b> Summon a minion
from your opponent's hand.
Your other Zerg minions gain
<b>Reborn</b> and attack it.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass