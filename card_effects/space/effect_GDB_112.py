"""Effect for Soulbound Spire (GDB_112).

Card Text: [x]<b>Deathrattle:</b> Summon a
minion with Cost equal to this
minion's Attack <i>(up to 10)</i>.
<b>Starship Piece</b>
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass