"""Effect for Carress, Cabaret Star (VAC_449t6).

Card Text: <b>Battlecry:</b> Deal 6 damage
to the enemy hero.
<b>Freeze</b> three random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 6, source)