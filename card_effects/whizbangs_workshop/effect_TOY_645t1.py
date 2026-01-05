"""Effect for Greater Opal Spellstone (TOY_645t1).

Card Text: Draw 3 cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)