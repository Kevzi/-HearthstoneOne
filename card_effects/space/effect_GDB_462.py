"""Effect for Orbital Satellite (GDB_462).

Card Text: [x]<b>Discover</b> a Draenei.
If you played an
adjacent card this turn,
<b>Discover</b> another.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass