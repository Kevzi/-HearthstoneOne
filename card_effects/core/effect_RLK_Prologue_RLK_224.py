"""Effect for Overseer Frigidara (RLK_Prologue_RLK_224).

Card Text: <b>Battlecry:</b> Draw 2 spells.
If they're both Frost spells, deal 2 damage to all enemies.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)
    # Draw 2 card(s)
    player.draw(2)