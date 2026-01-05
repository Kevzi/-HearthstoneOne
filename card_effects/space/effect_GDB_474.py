"""Effect for Warp Drive (GDB_474).

Card Text: Draw 2 cards. If you're building a <b>Starship</b>, they cost (2) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)