"""Effect for Nightshade Tea (VAC_404t2).

Card Text: Deal $2 damage
to a minion. Deal $2 damage to your hero.
<i>(Last Drink!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)