"""Effect for Divine Star (GDB_460).

Card Text: Deal $3 damage
to a minion. Give a random minion in your hand +3 Health.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 3, source)
    # Restore 3 Health
    if target:
        game.heal(target, 3, source)