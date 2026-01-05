"""Effect for Steamcleaner (CORE_REV_946).

Card Text: <b>Battlecry:</b> Destroy ALL cards in both players' decks that didn't start there.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()