"""Effect for GAME_005 (The Coin)"""

def setup(game, source):
    # The Coin logic is usually handled as an 'on_play' effect
    pass

def on_play(game, source, target):
    # Gain 1 temporary mana crystal
    source.controller.temp_mana += 1
