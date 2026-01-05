"""Effect for Assassinate (CORE_CS2_076).

Card Text: Destroy an enemy minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()