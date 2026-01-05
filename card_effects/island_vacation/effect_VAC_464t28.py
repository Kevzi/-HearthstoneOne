"""Effect for Vampiric Fangs (VAC_464t28).

Card Text: Destroy a minion. Restore its Health to your hero.
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