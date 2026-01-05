"""Effect for The 8 Hands From Beyond (GDB_477).

Card Text: <b>Battlecry:</b> Destroy both players' decks EXCEPT
the 8 highest Cost cards in each.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()