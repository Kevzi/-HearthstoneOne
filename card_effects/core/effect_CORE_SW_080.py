"""Effect for Cornelius Roame (CORE_SW_080).

Card Text: [x]At the start and end
 of each player's turn,
draw a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)