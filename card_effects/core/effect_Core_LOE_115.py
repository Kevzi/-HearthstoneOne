"""Effect for Raven Idol (Core_LOE_115).

Card Text: <b>Choose One -</b>
<b>Discover</b> a minion; or <b>Discover</b> a spell.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass