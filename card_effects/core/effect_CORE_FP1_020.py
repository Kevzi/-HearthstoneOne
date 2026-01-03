"""CORE_FP1_020 - Avenge: When one of your minions dies, give a random friendly minion +3/+2."""

def on_friendly_death(game, owner, secret, minion=None):
    if minion and minion.controller == owner:
        # Find another friendly minion to buff
        other_minions = [m for m in owner.board if m != minion and m.health > 0]
        if other_minions:
            import random
            target = random.choice(other_minions)
            target.attack += 3
            target.health += 2
            target.max_health += 2
            return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
