"""Effect for Sleet Skater (TOY_375t).

Card Text: <b>Mini</b>
<b>Battlecry:</b> <b>Freeze</b> an
enemy minion. Gain Armor equal to its Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 1 Armor
    player.hero.gain_armor(1)