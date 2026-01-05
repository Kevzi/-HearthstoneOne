"""Effect for Jettison (GDB_227).

Card Text: <b>Discover</b> a spell.
Spend 2 Armor to <b>Discover</b> another.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass