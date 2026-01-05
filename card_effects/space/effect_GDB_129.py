"""Effect for Doommaiden (GDB_129).

Card Text: [x]<b>Battlecry:</b> Draw a card from
your opponent's deck.
If you don't play it this
turn, put it back.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)