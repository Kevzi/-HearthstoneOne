"""Effect for Movement of Pride (ETC_085t2).

Card Text: Draw your highest
Cost minion. Reduce
its Cost by (6).
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 6 card(s)
    player.draw(6)