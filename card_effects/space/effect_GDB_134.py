"""Effect for Arkwing Pilot (GDB_134).

Card Text: At the end of your turn, deal 3 damage to a random enemy. <b><b>Spellburst</b>:</b> Summon an Arkwing Pilot.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 3, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass