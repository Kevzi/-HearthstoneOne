"""Effect for Coldlight Seer (CORE_EX1_103).

Card Text: <b>Battlecry:</b> Give your other Murlocs +2 Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)