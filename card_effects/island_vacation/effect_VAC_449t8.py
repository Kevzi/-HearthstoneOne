"""Effect for Carress, Cabaret Star (VAC_449t8).

Card Text: <b>Battlecry:</b> Deal 6 damage
to the enemy hero.
Restore 6 Health to your hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)
    # Restore 6 Health
    if target:
        game.heal(target, 6, source)