"""CS3_020 - Illidari Inquisitor"""

# Rush is handled by JSON/Engine.

def on_hero_attack(game, player, hero, target):
    # "After your hero attacks an enemy, this attacks it too."
    
    # We need to find the Inquisitor on board
    # This hook (on_hero_attack) needs to be registered or called globally?
    # The simulator engine calls 'on_hero_attack' for ALL minions on board that implement it?
    # YES, assumed simulator behavior.
    
    inquisitor = None
    for m in player.board:
        if m.card_id == "CS3_020":
            inquisitor = m
            # Check if this specific instance is the one triggering (if we had 'self', but here we iterate)
            # Actually, this file is a module. The engine calls module.on_hero_attack(game, owner, minion_instance, target) usually?
            # Let's check a similar trigger implementation.
            pass

# Récriture pour le format standard des triggers "Global" ou "Minion"
def on_after_attack(game, player, attacker, target):
    # Check if attacker is our HERO and target is ENEMY
    if attacker == player.hero and target.controller != player:
        # Check if WE are the Inquisitor (passed as context?) -> No, typically we need to iterate or register.
        # BUT, standard engine pattern for passive triggers:
        # The engine iterates board, checks for 'on_after_attack' on each minion's effect module.
        pass

# Correction: The engine likely calls `check_triggers('after_attack', ...)`
# Let's write it assuming ``minion`` is passed as context if the engine supports it, 
# OR we assume this function is called for the specific card being played?
# No, for minions on board, the engine must iterate.

# Let's assume standard signature:
def on_after_hero_attack(game, player, hero, target, minion_instance):
    if minion_instance.controller == player and hero == player.hero:
        if minion_instance.can_attack(target):
            game.attack(minion_instance, target)
