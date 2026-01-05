"""Effect for Libram of Clarity (GDB_137).

Card Text: Draw 2 minions.
If this costs (0), give them +2/+1.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)