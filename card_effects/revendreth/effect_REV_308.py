"""REV_308 - Maze Guide"""

def get_random_2_drop():
    # Use standard 2 drops: River Crocolisk (CS2_120), Bloodfen Raptor (CS2_172)
    import random
    return random.choice(["CS2_120", "CS2_172", "EX1_066", "CS2_121"])
    
def on_battlecry(game, player, card, target=None):
    # Summon a random 2-Cost minion.
    minion_id = get_random_2_drop()
    from simulator.factory import create_card
    minion = create_card(minion_id, game)
    if minion:
        player.summon(minion)
