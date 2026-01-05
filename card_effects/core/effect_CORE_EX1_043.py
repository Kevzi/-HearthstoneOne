"""Effect for Twilight Drake (CORE_EX1_043).

Card Text: <b>Battlecry:</b> Gain +1 Health for each card in your hand.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)