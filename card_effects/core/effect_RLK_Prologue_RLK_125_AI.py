"""Effect for Obliterate (RLK_Prologue_RLK_125_AI).

Card Text: Destroy a minion. Your hero takes damage equal to its Health.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)
    # Destroy target
    if target:
        target.destroy()