"""Effect for Liberator (SC_403b).

Card Text: [x]<b>Starship Piece</b>
When this is launched,
deal 2 damage to all
enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)