"""REV_011 - Demolition Renovator"""
def on_battlecry(game, player, card, target=None):
    # Destroy an enemy Location.
    # Locations are a specific type of entity. 
    # For now, we assume we can target them if they are on opponent board.
    if target and target.controller != player and getattr(target, 'card_type', None) == "LOCATION":
        target.destroy()
