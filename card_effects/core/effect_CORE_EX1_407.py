"""Effect for Brawl (CORE_EX1_407).

Card Text: Destroy all minions except one. <i>(chosen randomly)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()