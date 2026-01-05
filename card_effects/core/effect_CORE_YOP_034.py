"""Effect for Runaway Blackwing (CORE_YOP_034).

Card Text: [x]At the end of your turn,
deal 10 damage to a
random enemy minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 10 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 10, source)