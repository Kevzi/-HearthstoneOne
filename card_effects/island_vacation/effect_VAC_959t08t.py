"""Effect for Amulet of Energy (VAC_959t08t).

Card Text: Restore #12 Health
to your hero.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 12 Health
    if target:
        game.heal(target, 12, source)