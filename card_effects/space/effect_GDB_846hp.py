"""Effect for Tracking (GDB_846hp).

Card Text: <b>Discover</b> a card from your deck.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass