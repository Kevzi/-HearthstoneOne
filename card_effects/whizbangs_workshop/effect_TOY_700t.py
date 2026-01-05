"""Effect for Moment of Discovery (TOY_700t).

Card Text: [x]<b>Discover</b> a Druid spell,
a Druid minion, or a
Neutral minion you can
afford to play.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass