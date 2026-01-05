"""Effect for Carress, Cabaret Star (VAC_449t20).

Card Text: <b>Battlecry:</b> Deal 2 damage
to all enemy minions.
Destroy 2 random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)
    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()