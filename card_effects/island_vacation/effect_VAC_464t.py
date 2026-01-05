"""Effect for Eudora's Treasure Hunt (VAC_464t).

Card Text: <b>Sidequest:</b> Play 3 cards from other classes.
<b>Reward:</b> <b>Discover</b> two amazing pieces of loot!
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass