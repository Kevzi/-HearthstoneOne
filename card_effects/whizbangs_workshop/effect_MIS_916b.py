"""Effect for Paper! (MIS_916b).

Card Text: If your opponent chooses Rock,
you draw two cards.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)