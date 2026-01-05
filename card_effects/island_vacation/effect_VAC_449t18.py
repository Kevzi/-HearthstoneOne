"""Effect for Carress, Cabaret Star (VAC_449t18).

Card Text: <b>Battlecry:</b> Restore 6 Health to your hero.
Destroy 2 random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 6 Health
    if target:
        game.heal(target, 6, source)
    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()