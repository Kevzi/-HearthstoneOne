"""Effect for Conservative Forecast (WORK_025b).

Card Text: +2 Health.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)