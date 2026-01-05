"""Effect for Carress, Cabaret Star (VAC_449t5).

Card Text: <b>Battlecry:</b> Draw 2 cards.
Deal 2 damage to all enemy minions.
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