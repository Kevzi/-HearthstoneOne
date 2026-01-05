"""Effect for Dalaran Brochure (WORK_050t).

Card Text: [x]Draw two spells.
They cost (1) less.
<i>(Flips each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)