"""Effect for Baneling (SC_019t).

Card Text: <b>Deathrattle:</b> Deal
damage equal to this minion's Attack to all enemy minions.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 1, source)
    game.deal_damage(opponent.hero, 1, source)