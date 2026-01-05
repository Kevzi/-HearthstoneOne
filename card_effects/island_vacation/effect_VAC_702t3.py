"""Effect for Wondrous Wand (VAC_702t3).

Card Text: Draw 3 cards. Reduce
their Costs by (3).
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)