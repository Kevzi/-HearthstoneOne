"""Effect for Horseman's Head (TOY_829t).

Card Text: [x]<b>When Drawn, this Casts</b>
and your enemy will <i>cower!</i>
Imbue the souls of Undead
into your <i>Hero Power!</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)