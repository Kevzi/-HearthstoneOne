"""Effect for Opal Spellstone (TOY_645t).

Card Text: Draw 2 cards.
<i>(Attack with your hero
2 times to upgrade.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)