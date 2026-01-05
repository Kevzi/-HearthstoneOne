"""Effect for Carrier (SC_756).

Card Text: [x]At the end of your turn,
summon four 4/1
Interceptors that attack
random enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass