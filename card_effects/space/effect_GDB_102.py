"""Effect for Starship Schematic (GDB_102).

Card Text: <b>Discover</b> a <b>Starship Piece</b> from another class. It costs (1) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass