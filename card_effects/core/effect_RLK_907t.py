"""Effect for Rime Elemental (RLK_907t).

Card Text: <b>Deathrattle:</b> Deal 2 damage to a random enemy.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)