"""Effect for The Curator (CORE_KAR_061).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Draw a Beast, Dragon, and Murloc from your deck.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)