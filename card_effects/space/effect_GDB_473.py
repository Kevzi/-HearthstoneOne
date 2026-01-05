"""Effect for Headhunt (GDB_473).

Card Text: Deal $2 damage. Get a 4/4 Crewmate with a random <b>Bonus Effect</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)