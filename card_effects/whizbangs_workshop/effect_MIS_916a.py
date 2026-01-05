"""Effect for Rock! (MIS_916a).

Card Text: If your opponent chooses Scissors,
you draw two cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)