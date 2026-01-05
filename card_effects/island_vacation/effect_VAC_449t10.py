"""Effect for Carress, Cabaret Star (VAC_449t10).

Card Text: <b>Battlecry:</b> Deal 6 damage
to the enemy hero.
Deal 2 damage to all enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 6, source)
    game.deal_damage(opponent.hero, 6, source)