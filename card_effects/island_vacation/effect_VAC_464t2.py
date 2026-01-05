"""Effect for Necrotic Poison (VAC_464t2).

Card Text: Destroy a minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()