"""Effect for Final Frontier (GDB_857).

Card Text: <b>Discover</b> a 10-Cost minion from the past. Set its Cost to (1).
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass