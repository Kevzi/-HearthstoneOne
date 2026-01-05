"""Effect for Rangari Scout (GDB_841).

Card Text: After you <b>Discover</b> a card, get a copy of it.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass