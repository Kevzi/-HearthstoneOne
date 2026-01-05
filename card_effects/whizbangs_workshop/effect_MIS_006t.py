"""Effect for Toysnatching Geist (MIS_006t).

Card Text: [x]<b>Gigantic</b>
<b>Battlecry:</b> <b>Discover</b> an
Undead. Reduce its Cost by
this minion's Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass