"""Effect for Lucky Comet (GDB_873).

Card Text: <b>Discover</b> a <b>Combo</b> minion. The next one
you play triggers its <b>Combo</b> twice.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass