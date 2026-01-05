"""Effect for Obsidian Statue (CORE_ICC_214).

Card Text: [x]<b>Taunt, Lifesteal</b>
<b>Deathrattle:</b> Destroy a
 random enemy minion.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Destroy a random enemy minion
    import random
    if opponent.board:
        target = random.choice(opponent.board)
        target.destroy()