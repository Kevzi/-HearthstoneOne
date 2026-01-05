"""Effect for The Headless Horseman (TOY_829t2).

Card Text: [x]<b>Battlecry:</b> Destroy the enemy
minion with the most <i>Attack!</i>
Shuffle my Head into your
deck, you must get it <i>back!</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()