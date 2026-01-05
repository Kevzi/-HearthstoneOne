"""Effect for Redscale Dragontamer (CORE_DMF_194).

Card Text: <b>Deathrattle:</b> Draw a Dragon.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)