"""Effect for Ravage (SC_004hp).

Card Text: [x]Deal $3 damage randomly
split among all enemies.
<i>(Improved by Zerg minions
you control!)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 3, source)
    game.deal_damage(opponent.hero, 3, source)