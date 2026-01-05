"""Effect for Carress, Cabaret Star (VAC_449t7).

Card Text: [x]<b>Battlecry:</b> Deal 6 damage
to the enemy hero.
Gain +2/+2 and <b>Taunt</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)