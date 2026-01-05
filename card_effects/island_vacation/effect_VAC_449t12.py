"""Effect for Carress, Cabaret Star (VAC_449t12).

Card Text: <b>Battlecry:</b> Restore 6
Health to your hero.
<b>Freeze</b> three random
enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 6 Health
    if target:
        game.heal(target, 6, source)