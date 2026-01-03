
from simulator.entities import Card, Player
from simulator.game import Game

def on_play(game: Game, player: Player, card: Card, target=None):
    player.next_spell_cost_reduction = 2
