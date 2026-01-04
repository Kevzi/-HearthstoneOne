"""TLC_436 - Reanimated Pterrordax"""
# Costs Corpses instead of Mana. 
# This logic is usually handled in 'get_cost' inside the simulator.
# But we can add a flag here for the simulator to see.

def get_alternative_cost(game, card):
    # Costs Corpses equal to original mana cost
    return {"type": "CORPSES", "amount": card.base_cost}
