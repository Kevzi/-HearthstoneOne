"""Effect for Veranus (CORE_DRG_095).

Card Text: <b>Battlecry:</b> Change the Health of all enemy minions to 1.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)