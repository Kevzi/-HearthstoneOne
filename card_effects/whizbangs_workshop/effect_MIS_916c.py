"""Effect for Scissors! (MIS_916c).

Card Text: If your opponent chooses Paper,
you draw two cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)