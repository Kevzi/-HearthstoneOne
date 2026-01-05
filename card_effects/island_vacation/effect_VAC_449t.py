"""Effect for Carress, Cabaret Star (VAC_449t).

Card Text: <b>Battlecry:</b> Draw 2 cards.
Deal 6 damage to the enemy hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)
    # Draw 2 card(s)
    player.draw(2)