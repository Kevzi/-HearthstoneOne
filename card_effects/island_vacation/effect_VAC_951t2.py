"""Effect for "Health" Drink (VAC_951t2).

Card Text: <b>Lifesteal</b>. Deal $3 damage to a minion.
<i>(Last Drink!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)