"""Effect for Stalwart Avenger (GDB_230).

Card Text: <b>Immune</b> while attacking.
At the end of EACH turn, swap this minion's Attack and Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)