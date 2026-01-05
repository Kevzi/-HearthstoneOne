"""Effect for Ice Sculpture (VAC_305t).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Gain 4 Armor.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Gain 4 Armor
    player.hero.gain_armor(4)