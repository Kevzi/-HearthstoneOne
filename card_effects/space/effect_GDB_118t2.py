"""Effect for Star of Conclusion (GDB_118t2).

Card Text: Once this is next to Star of Origination, deal $5 damage to all enemies.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 5, source)
    game.deal_damage(opponent.hero, 5, source)