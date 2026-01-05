"""Effect for Haywire Module (TOY_330t93).

Card Text: [x]At the end of your turn,
deal 3 damage to your hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)