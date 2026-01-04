"""EDR_456 - Darkrider"""
from simulator.enums import Race

def on_battlecry(game, player, card, target=None):
    # If holding a Dragon, Discover a Dragon with a Dark Gift.
    holding_dragon = any(c.is_minion and c.race == Race.DRAGON for c in player.hand if c is not card)
    
    if holding_dragon:
        # Discover a Dragon (from pool of dragons)
        dragons = [c for c in game.card_db if c.is_minion and c.race == Race.DRAGON]
        game.discover_card(player, dragons, source_card=card)

def on_discover_selection(game, player, card, choice):
    from simulator.factory import create_card
    copy = create_card(choice.card_id, game)
    if copy:
        # Give it a Dark Gift (Effect usually handled by buffing it)
        copy.add_buff("DARK_GIFT") # Hypothetical buff in simulator
        player.add_to_hand(copy)
