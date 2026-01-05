"""Effect for Sneed's Old Shredder (CORE_GVG_114).

Card Text: <b>Deathrattle:</b> Summon a random <b>Legendary</b> minion.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass