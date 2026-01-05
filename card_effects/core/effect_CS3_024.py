"""Effect for Taelan Fordring (CS3_024).

Card Text: [x]<b><b>Taunt</b>, Divine Shield</b>
<b>Deathrattle:</b> Draw your
highest Cost minion.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)