"""Effect for Finja, the Flying Star (CORE_CFM_344).

Card Text: [x]<b>Stealth</b>
   Whenever this attacks and   
kills a minion, summon 2
 Murlocs from your deck.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass