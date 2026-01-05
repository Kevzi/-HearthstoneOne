"""Effect for Pure Cold (VAC_464t5).

Card Text: Deal $8 damage to the enemy hero, and <b>Freeze</b> it.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 8 damage to target
    if target:
        game.deal_damage(target, 8, source)