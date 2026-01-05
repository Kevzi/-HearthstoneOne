"""Effect for Harbinger of Winter (RLK_Prologue_RLK_511).

Card Text: <b>Deathrattle:</b> Draw a
Frost spell.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)