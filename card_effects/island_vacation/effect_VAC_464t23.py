"""Effect for Embers of Ragnaros (VAC_464t23).

Card Text: Shoot three fireballs at random enemies that deal $8 damage each.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 8 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 8, source)