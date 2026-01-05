"""Effect for Mo'arg Forgefiend (SW_068_COPY).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Gain 8 Armor.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Gain 8 Armor
    player.hero.gain_armor(8)