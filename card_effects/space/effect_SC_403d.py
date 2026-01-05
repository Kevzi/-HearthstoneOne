"""Effect for Banshee (SC_403d).

Card Text: <b>Starship Piece</b>
When this is launched,
deal 3 damage to a random enemy.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 3, source)