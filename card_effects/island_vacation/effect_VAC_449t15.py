"""Effect for Carress, Cabaret Star (VAC_449t15).

Card Text: <b>Battlecry:</b> Gain +2/+2
and <b>Taunt</b>.
Restore 6 Health to your hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)