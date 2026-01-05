"""Effect for Deathchiller (CORE_RLK_083).

Card Text: [x]After you cast a spell,
deal 1 damage to two
random enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 1, source)