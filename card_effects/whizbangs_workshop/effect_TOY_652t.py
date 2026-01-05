"""Effect for Window Shopper (TOY_652t).

Card Text: [x]<b>Mini</b>
<b>Battlecry:</b> <b>Discover</b> a
Demon. Set its stats and
Cost to this minion's.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass