"""Effect for Movement of Greed (ETC_085t7).

Card Text: Draw 6 cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 6 card(s)
    player.draw(6)