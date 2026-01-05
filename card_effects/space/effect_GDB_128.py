"""Effect for Archimonde (GDB_128).

Card Text: [x]<b>Battlecry:</b> Summon every
Demon you played this
game that didn't start
in your deck.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass