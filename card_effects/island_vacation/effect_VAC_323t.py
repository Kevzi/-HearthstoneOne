"""Effect for Malted Magma (VAC_323t).

Card Text: Deal $1 damage to
all enemy minions.
<i>(2 Drinks left!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 1, source)
    game.deal_damage(opponent.hero, 1, source)