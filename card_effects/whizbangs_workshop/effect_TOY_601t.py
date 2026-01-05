"""Effect for Factory Assemblybot (TOY_601t).

Card Text: <b>Mini</b>
At the end of your turn, summon a 6/7 Bot that attacks a random enemy.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass