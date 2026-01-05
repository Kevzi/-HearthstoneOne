"""Effect for Carress, Cabaret Star (VAC_449t19).

Card Text: <b>Battlecry:</b> Restore 6 Health to your hero.
Deal 2 damage to all enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 6, source)
    game.deal_damage(opponent.hero, 6, source)
    # Restore 6 Health
    if target:
        game.heal(target, 6, source)