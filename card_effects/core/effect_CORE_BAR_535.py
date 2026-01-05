"""Effect for Thickhide Kodo (CORE_BAR_535).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Gain 5 Armor.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Gain 5 Armor
    player.hero.gain_armor(5)