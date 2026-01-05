"""Effect for Tolin's Goblet (VAC_702t2).

Card Text: Draw a card. Fill your hand with copies of it.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)