"""Effect for Asteroid (GDB_430).

Card Text: <b>Casts When Drawn</b>
Deal $2 damage to a random enemy.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)
    # Draw 2 card(s)
    player.draw(2)