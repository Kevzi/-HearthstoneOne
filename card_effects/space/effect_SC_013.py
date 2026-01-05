"""Effect for Grunty (SC_013).

Card Text: [x]<b>Battlecry:</b> Summon four
random Murlocs, then shoot
them at enemy minions.
 <i>(You pick the targets!)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass