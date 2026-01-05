"""Effect for Thassarian (RLK_Prologue_RLK_223).

Card Text: <b>Reborn</b>
<b>Battlecry and Deathrattle:</b> Deal 2 damage to a random enemy.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 2, source)