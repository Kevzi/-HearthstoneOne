"""Effect for Cat Constellation (VAC_907t1).

Card Text: Draw 2 cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)