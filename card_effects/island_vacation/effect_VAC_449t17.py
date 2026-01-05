"""Effect for Carress, Cabaret Star (VAC_449t17).

Card Text: <b>Battlecry:</b> Gain +2/+2
and <b>Taunt</b>.
Deal 2 damage to all enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)