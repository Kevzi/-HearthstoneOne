"""Effect for Far Sight (CORE_CS2_053).

Card Text: Draw a card. That card costs (3) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)