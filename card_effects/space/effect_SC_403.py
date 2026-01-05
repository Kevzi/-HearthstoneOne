"""Effect for Starport (SC_403).

Card Text: [x]Summon a 2/1
<b>Starship Piece</b> with an
effect when launched.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass