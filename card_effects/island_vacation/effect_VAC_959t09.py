"""Effect for Amulet of Mobility (VAC_959t09).

Card Text: Draw 3 cards.
<i>(Discard 2 of them!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)