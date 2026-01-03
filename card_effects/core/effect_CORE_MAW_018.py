"""CORE_MAW_018 - Perjury: When your turn starts, Discover and cast a Secret from another class."""

def on_turn_start(game, owner, secret):
    # Simplified: just add a random secret from another class
    import random
    from simulator.factory import create_card
    
    secret_ids = ["CORE_EX1_287", "CORE_EX1_289", "CORE_EX1_610", "CORE_EX1_611", "CORE_EX1_130"]
    chosen_id = random.choice(secret_ids)
    
    chosen = create_card(chosen_id, game)
    if chosen and len(owner.secrets) < 5:
        owner.secrets.append(chosen)
    return True

def on_play(game, player, card, target=None):
    player.secrets.append(card)
