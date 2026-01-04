
from simulator.entities import Card
from simulator.player import Player
from simulator.game import Game
from simulator.enums import Race

def on_play(game: Game, player: Player, card: Card, target=None):
    # Register the trigger when played
    game.register_trigger("on_minion_summon", card, on_summon_trigger)

def on_summon_trigger(game: Game, owner_card: Card, summoned_minion: Card):
    # Only if the owner of the card is the one who summoned
    if owner_card.controller == summoned_minion.controller:
        # Check if summoned is Elemental
        if Race.ELEMENTAL in summoned_minion.races:
            enemies = game.get_enemy_targets(owner_card.controller, include_hero=True)
            if enemies:
                target = game.random.choice(enemies)
                game.deal_damage(target, 3, source=owner_card)
