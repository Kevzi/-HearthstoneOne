"""Effect for Roach (SC_012).

Card Text: When you draw this, get a copy of it. <b>Battlecry:</b> If you control another Zerg minion, gain +1/+2.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)