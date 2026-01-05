"""Effect for Cultivate (TOY_801a).

Card Text: Draw a spell.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)