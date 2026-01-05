"""Effect for Book of the Dead (VAC_464t24).

Card Text: Deal $7 damage to all enemies. Costs (1) less for each minion that's died this game.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 7 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 7, source)
    game.deal_damage(opponent.hero, 7, source)