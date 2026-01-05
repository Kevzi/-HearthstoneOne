"""Effect for Lurker (SC_009).

Card Text: [x]After a friendly minion
attacks, deal 1 damage to a
random enemy <i>(or 2 if your
minion is a Zerg)</i>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 1, source)