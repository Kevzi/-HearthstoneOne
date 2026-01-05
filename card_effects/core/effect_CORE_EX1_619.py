"""Effect for Equality (CORE_EX1_619).

Card Text: Change the Health of ALL minions to 1.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)