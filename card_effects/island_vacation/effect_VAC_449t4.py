"""Effect for Carress, Cabaret Star (VAC_449t4).

Card Text: <b>Battlecry:</b> Draw 2 cards.
Destroy 2 random
enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()