"""Effect for Loot Hoarder (CORE_EX1_096).

Card Text: <b>Deathrattle:</b> Draw a card.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)