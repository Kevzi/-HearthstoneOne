"""Effect for Delicious Cheese (VAC_955t).

Card Text: Summon three random 1-Cost minions. <i>(Upgrades each turn!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass