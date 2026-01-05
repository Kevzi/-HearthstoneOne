"""Effect for Crazed Alchemist (CORE_EX1_059).

Card Text: <b>Battlecry:</b> Swap the Attack and Health of a minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)