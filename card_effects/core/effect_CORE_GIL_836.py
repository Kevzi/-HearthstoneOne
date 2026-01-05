"""Effect for Blazing Invocation (CORE_GIL_836).

Card Text: [x]<b>Discover</b> a <b>Battlecry</b>
minion. It costs (1) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass