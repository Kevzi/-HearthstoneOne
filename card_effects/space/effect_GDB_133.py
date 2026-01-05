"""Effect for Pocket Dimension (GDB_133).

Card Text: <b>Discover</b> a spell.
Repeat until you see one for the second time.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass