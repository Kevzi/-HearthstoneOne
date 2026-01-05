"""Effect for Falric (CORE_EDR_003).

Card Text: You gain twice as many
<b>Corpses</b> as normal.
<b>Battlecry:</b> Draw a card that spends <b>Corpses</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)