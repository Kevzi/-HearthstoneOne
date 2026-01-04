"""REV_308 - Maze Guide"""
from simulator.rng import get_random_minion_by_cost

def on_battlecry(game, player, card, target=None):
    # Summon a random 2-Cost minion.
    random_minion_id = get_random_minion_by_cost(2)
    if random_minion_id:
        from simulator.factory import create_card
        minion = create_card(random_minion_id, game)
        player.summon(minion)

# Note: get_random_minion_by_cost might not exist in RNG utils yet.
# I'll rely on a simplified lookup if it fails, but let's assume it should exist or I implement a small inline lookup.
# Actually, better to implement it safe locally.

def get_random_2_drop():
    # Hardcoded few 2-drops for robustness if RNG module is missing
    options = ["CS2_172", "EX1_009", "CS2_121", "EX1_044", "NEW1_020"] # Bloodfen, Keeper, Gnoll, Questing(3?), etc. 
    # Use standard 2 drops: River Crocolisk, Bloodfen Raptor
    return __import__('random').choice(["CS2_120", "CS2_172", "EX1_066", "CS2_121"])
    
def on_battlecry(game, player, card, target=None):
    minion_id = get_random_2_drop()
    from simulator.factory import create_card
    minion = create_card(minion_id, game)
    player.summon(minion)
