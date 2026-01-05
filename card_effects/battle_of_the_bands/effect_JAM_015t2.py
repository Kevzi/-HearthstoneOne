"""Effect for Reinforced Tuning Fork (JAM_015t2).

Card Text: [x]<b>Battlecry:</b> Gain 5 Armor.
<i>(Changes each turn.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 5 Armor
    player.hero.gain_armor(5)