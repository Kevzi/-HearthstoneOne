"""Effect for Gravity Lapse (GDB_464).

Card Text: Set EVERY minion's Attack and Health to the lower of the two.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)