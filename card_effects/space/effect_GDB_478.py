"""Effect for Assimilating Blight (GDB_478).

Card Text: <b>Discover</b> a 3-Cost <b>Deathrattle</b> minion. Summon it with <b>Reborn</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Discover effect
    # TODO: Implement discover with proper card pool
    pass