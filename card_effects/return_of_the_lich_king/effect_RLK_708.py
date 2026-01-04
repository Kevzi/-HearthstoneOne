"""RLK_708 - Chillfallen Baron"""

def on_battlecry(game, player, card, target=None):
    player.draw()

def on_deathrattle(game, minion):
    owner = minion.controller
    owner.draw()
