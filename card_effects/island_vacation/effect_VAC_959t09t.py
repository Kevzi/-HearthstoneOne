"""Effect for Amulet of Mobility (VAC_959t09t).

Card Text: Draw 3 cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)