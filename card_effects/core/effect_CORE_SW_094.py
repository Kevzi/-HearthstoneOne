"""Effect for Heavy Plate (CORE_SW_094).

Card Text: <b>Tradeable</b>
Gain 8 Armor.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 8 Armor
    player.hero.gain_armor(8)