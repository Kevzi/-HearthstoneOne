"""CORE_BAR_812 - Oasis Ally: When a friendly minion is attacked, summon a 3/6 Water Elemental."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    if defender and defender.controller == owner and defender.card_type.name == 'MINION':
        if len(owner.board) < 7:
            from simulator.factory import create_card
            from simulator.entities import Minion
            
            elemental = create_card("CS2_033", game)  # Water Elemental
            if elemental:
                minion = Minion(elemental.data, game)
                minion.controller = owner
                owner.summon(minion)
            return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
