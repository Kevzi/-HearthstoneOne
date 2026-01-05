"""Effect for Feral Rage (CORE_OG_047).

Card Text: <b>Choose One -</b> Give your hero +4 Attack this turn; or Gain 8 Armor.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 4 Armor
    player.hero.gain_armor(4)