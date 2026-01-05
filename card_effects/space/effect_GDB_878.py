"""Effect for Braingill (GDB_878).

Card Text: <b>Battlecry:</b> Give your other Murlocs "<b>Deathrattle:</b> Draw a card."
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)