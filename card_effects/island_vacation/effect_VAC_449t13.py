"""Effect for Carress, Cabaret Star (VAC_449t13).

Card Text: <b>Battlecry:</b> Destroy two
random enemy minions. <b>Freeze</b> three random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()