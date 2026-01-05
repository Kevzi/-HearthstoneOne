"""Effect for Askara (GDB_455).

Card Text: <b>Battlecry:</b> The next Draenei you play summons a copy of itself.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass