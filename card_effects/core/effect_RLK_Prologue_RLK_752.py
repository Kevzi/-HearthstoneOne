"""Effect for Rime Sculptor (RLK_Prologue_RLK_752).

Card Text: [x]<b>Battlecry:</b> Summon two
2/1 Rime Elementals with
"<b>Deathrattle:</b> Deal 2 damage
to a random enemy."
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass