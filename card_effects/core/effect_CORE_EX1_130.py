"""CORE_EX1_130 - Noble Sacrifice: Summon a 2/1 Defender when enemy attacks."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    if attacker and attacker.controller != owner and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        defender_card = create_card("CS2_231", game)
        if defender_card:
            m = Minion(defender_card.data, game)
            m.attack = 2
            m.health = 1
            m.max_health = 1
            m.name = "Defender"
            m.controller = owner
            owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
