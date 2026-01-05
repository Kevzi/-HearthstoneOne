"""Effect for Marrow Manipulator (CORE_RLK_505).

Card Text: [x]<b>Battlecry:</b> Spend up to 5
<b>Corpses</b>. Deal 2 damage to
a random enemy for each.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 5, source)