"""Effect for Carress, Cabaret Star (VAC_449t2).

Card Text: <b>Battlecry:</b> Draw 2 cards.
Gain +2/+2 and <b>Taunt</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)