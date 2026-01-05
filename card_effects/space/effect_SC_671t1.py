"""Effect for Archon (SC_671t1).

Card Text: [x]At the end of your turn,
deal 8 damage to the
enemy hero and 2 damage
to their minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 8 damage to target
    if target:
        game.deal_damage(target, 8, source)