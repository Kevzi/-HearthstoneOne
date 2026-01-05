"""Effect for Patchwerk (RLK_Prologue_RLK_071).

Card Text: [x]<b>Battlecry:</b> Destroy a random
minion in your opponent's
 hand, deck, and battlefield. 
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()