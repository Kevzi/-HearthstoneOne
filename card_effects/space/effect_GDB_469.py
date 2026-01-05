"""Effect for Auchenai Death-Speaker (GDB_469).

Card Text: [x]After another friendly
minion is <b>Reborn</b>,
summon a copy of it.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass