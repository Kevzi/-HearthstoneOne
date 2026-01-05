"""Effect for Chillfallen Baron (RLK_Prologue_RLK_708).

Card Text: <b>Battlecry and Deathrattle:</b> Draw a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)