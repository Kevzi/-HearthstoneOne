"""Effect for Star Grazer (GDB_855).

Card Text: <b>Elusive, Taunt</b>
<b>Spellburst:</b> Give your
hero +8 Attack this turn and gain 8 Armor.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 8 Armor
    player.hero.gain_armor(8)