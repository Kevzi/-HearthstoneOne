"""Effect for Carress, Cabaret Star (VAC_449t16).

Card Text: <b>Battlecry:</b> Gain +2/+2
and <b>Taunt</b>.
Destroy 2 random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()