"""CORE_EX1_611 - Freezing Trap: When an enemy minion attacks, return it to its owner's hand. It costs (2) more."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    if attacker and attacker.controller != owner and attacker.card_type.name == 'MINION':
        # Return to hand
        attacker.controller.board.remove(attacker)
        attacker.zone = game.enums.Zone.HAND if hasattr(game, 'enums') else None
        attacker.cost += 2  # Costs 2 more
        attacker.controller.hand.append(attacker)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
