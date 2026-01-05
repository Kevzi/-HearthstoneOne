"""Effect for Yamato Cannon (SC_406).

Card Text: [x]<b>Starship Piece</b>
<b>Battlecry:</b> Destroy a random
enemy minion. Also triggers
on launch.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()