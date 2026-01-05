"""Effect for Captain's Log (GDB_228).

Card Text: Draw 2 cards.
Costs (1) less for each Draenei you control.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)