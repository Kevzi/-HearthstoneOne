"""Effect for The Gravitational Displacer (GDB_466).

Card Text: [x]<b>Starship Piece</b>
When this is launched,
summon a copy of
the <b>Starship</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass