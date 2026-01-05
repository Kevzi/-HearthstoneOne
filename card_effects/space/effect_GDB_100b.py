"""Effect for Offensive Formation (GDB_100b).

Card Text: Deal damage equal to the <b>Starship's</b> Attack randomly split between all enemies.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 1, source)
    game.deal_damage(opponent.hero, 1, source)