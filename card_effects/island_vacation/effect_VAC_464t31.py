"""Effect for Quel'Delar (VAC_464t31).

Card Text: After your hero attacks, deal 4 damage to all enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 4 damage to target
    if target:
        game.deal_damage(target, 4, source)