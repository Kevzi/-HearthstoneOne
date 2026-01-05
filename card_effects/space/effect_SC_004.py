"""Effect for Kerrigan, Queen of Blades (SC_004).

Card Text: [x]<b>Battlecry:</b> Summon two
2/5 Hive Queens. Deal 3
damage to all enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass