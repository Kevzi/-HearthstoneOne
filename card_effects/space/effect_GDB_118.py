"""Effect for Xor'toth, Breaker of Stars (GDB_118).

Card Text: [x]<b>Battlecry:</b> Add two Stars
   to both sides of your hand.   
When they collide, deal 5
damage to all enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 5, source)
    game.deal_damage(opponent.hero, 5, source)