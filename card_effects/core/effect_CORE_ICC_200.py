"""CORE_ICC_200 - Venomstrike Trap: When a minion is attacked, summon a 2/3 Poisonous Cobra."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    if defender and defender.controller == owner and defender.card_type.name == 'MINION':
        if len(owner.board) < 7:
            from simulator.factory import create_card
            from simulator.entities import Minion
            
            cobra = create_card("CS2_231", game)
            if cobra:
                m = Minion(cobra.data, game)
                m.attack = 2
                m.health = 3
                m.max_health = 3
                m.name = "Emperor Cobra"
                m._poisonous = True
                m.controller = owner
                owner.summon(m)
            return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
