"""Effect for Wand of Disintegration (VAC_464t16).

Card Text: <b>Silence</b> and destroy all enemy minions.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()