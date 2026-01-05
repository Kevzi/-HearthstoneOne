"""Effect for Repulsive Gargantuan (RLK_Prologue_RLK_115).

Card Text: Enemy characters
can't be healed.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)