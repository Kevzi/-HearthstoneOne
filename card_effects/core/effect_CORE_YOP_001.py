"""Effect for Illidari Studies (CORE_YOP_001).

Card Text: <b>Discover</b> an <b>Outcast</b> card. Your next one costs (1) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass