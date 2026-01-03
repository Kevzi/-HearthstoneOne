"""CORE_REV_828 - Kidnap: After opponent plays a minion, stuff it in a 0/4 Sack."""

def on_minion_played(game, owner, secret, minion=None):
    if minion:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        # Transform minion into a 0/4 Sack (simplified: just set stats)
        minion.attack = 0
        minion.health = 4
        minion.max_health = 4
        minion.name = "Sack"
        minion._taunt = False
        minion._divine_shield = False
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
