"""Effect for Eruption (VAC_321t).

Card Text: [x]<b>Casts When Drawn</b>
Deal $1 damage to
all enemies.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 1, source)
    game.deal_damage(opponent.hero, 1, source)
    # Draw 1 card(s)
    player.draw(1)