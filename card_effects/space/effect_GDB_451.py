"""Effect for Triangulate (GDB_451).

Card Text: [x]<b>Discover</b> a different
spell from your deck.
Shuffle 3 copies of it
into your deck.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass