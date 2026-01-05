"""Effect for Crusty the Crustacean (VAC_464t8).

Card Text: [x]<b>Battlecry:</b> Destroy a minion.
Gain its Attack and Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)
    # Destroy target
    if target:
        target.destroy()