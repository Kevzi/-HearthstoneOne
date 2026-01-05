"""Effect for Suffocate (GDB_476).

Card Text: Destroy a minion. If you're building a <b>Starship</b>, also destroy a random neighbor.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()