"""Effect for GAME_005 (The Coin)"""

def setup(game, source):
    pass

def on_play(game, source, target):
    source.controller.temp_mana += 1
