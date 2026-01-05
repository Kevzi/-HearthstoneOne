"""Effect for Defrost (RLK_Prologue_RLK_101).

Card Text: Draw a card.
Spend 2 <b>Corpses</b> to draw another.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)