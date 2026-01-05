"""Effect for I Know a Guy (CORE_WON_350).

Card Text: <b>Discover</b> a <b>Taunt</b> minion. Give it +1/+2.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass