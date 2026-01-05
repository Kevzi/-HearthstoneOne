"""Effect for Carress, Cabaret Star (VAC_449t9).

Card Text: <b>Battlecry:</b> Deal 6 damage
to the enemy hero.
Destroy 2 random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 6, source)
    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()