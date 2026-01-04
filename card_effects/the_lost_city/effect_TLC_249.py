"""TLC_249 - Sizzling Cinder"""
def on_deathrattle(game, minion):
    # Deal 2 damage randomly split among all enemies.
    game.deal_random_damage(minion.controller.opponent, 2, source=minion)
