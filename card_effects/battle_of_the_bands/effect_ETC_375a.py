"""Effect for Friendly Face (ETC_375a).

Card Text: Draw a Beast.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)