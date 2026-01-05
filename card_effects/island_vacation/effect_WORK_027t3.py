"""Effect for Hectic Tour (WORK_027t3).

Card Text: Get 2 random cards that can potentially deal damage to the enemy hero.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)