"""Effect for Fogsail Freebooter (CS3_022).

Card Text: <b>Battlecry:</b> If you have a weapon equipped, deal 2 damage.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)