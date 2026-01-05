"""Effect for Solar Flare (GDB_305).

Card Text: Deal $2 damage to all enemies. Costs (1) less for each Elemental you control.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)