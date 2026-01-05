"""Effect for Hematurge (CORE_RLK_066).

Card Text: <b>Battlecry:</b> Spend a
<b>Corpse</b> to <b>Discover</b> a
Blood Rune card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass