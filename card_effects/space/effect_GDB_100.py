"""Effect for Arkonite Defense Crystal (GDB_100).

Card Text: <b>Deathrattle:</b> Gain 4 Armor. <b>Starship Piece</b>
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Gain 4 Armor
    player.hero.gain_armor(4)