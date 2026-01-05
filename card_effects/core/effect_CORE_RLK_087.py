"""Effect for Asphyxiate (CORE_RLK_087).

Card Text: Destroy the highest Attack enemy minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()