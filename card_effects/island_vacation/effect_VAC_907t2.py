"""Effect for Bear Constellation (VAC_907t2).

Card Text: Gain 5 Armor.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 5 Armor
    player.hero.gain_armor(5)