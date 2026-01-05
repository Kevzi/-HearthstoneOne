"""Effect for Viking (SC_403a).

Card Text: <b>Starship Piece</b>
When this is launched, gain 5 Armor.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 5 Armor
    player.hero.gain_armor(5)