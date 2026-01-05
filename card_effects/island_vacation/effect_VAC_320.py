"""Effect for Seafloor Trawler (VAC_320).

Card Text: <b>Battlecry</b>: <b>Dredge</b>. Each player draws a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)