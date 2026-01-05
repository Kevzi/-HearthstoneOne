"""Effect for Moonstone Mauler (GDB_435).

Card Text: [x]<b>Battlecry:</b> Shuffle 3
Asteroids into your deck that
deal 2 damage to a random
enemy when drawn.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 3, source)
    # Draw 3 card(s)
    player.draw(3)