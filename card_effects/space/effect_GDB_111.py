"""Effect for Biopod (GDB_111).

Card Text: <b>Deathrattle:</b> Deal damage equal to this minion's Attack to a random enemy. <b>Starship Piece</b>
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 1, source)