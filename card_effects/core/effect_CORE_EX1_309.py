"""Effect for Siphon Soul (CORE_EX1_309).

Card Text: Destroy a minion. Restore #3 Health to your hero.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 3 Health
    if target:
        game.heal(target, 3, source)
    # Destroy target
    if target:
        target.destroy()