"""Effect for Star of Origination (GDB_118t).

Card Text: Once this is next to Star of Conclusion, deal $5 damage to all enemies.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 5, source)
    game.deal_damage(opponent.hero, 5, source)