"""Effect for Seabreeze Chalice (VAC_520t).

Card Text: Deal $2 damage randomly split among
all enemy minions.
<i>(2 Drinks left!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)