"""Effect for Nebula (GDB_479).

Card Text: [x]<b>Discover</b> two 8-Cost
minions to summon with
<b>Taunt</b> and <b>Elusive</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Discover effect
    # TODO: Implement discover with proper card pool
    pass