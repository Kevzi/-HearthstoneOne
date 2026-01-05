"""Effect for Frostmourne (CORE_RLK_086).

Card Text: <b>Deathrattle:</b> Summon every minion killed by this weapon.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass