"""Effect for Movement of Desire (ETC_085t6).

Card Text: [x]<b>Lifesteal</b>
Deal $6 damage to
the enemy hero.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)