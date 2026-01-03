"""CORE_REV_516 - Vengeful Visage: After enemy minion attacks hero, summon a copy to attack enemy hero."""

def on_hero_attacked(game, owner, secret, attacker=None, defender=None):
    if defender and defender == owner.hero and attacker and attacker.card_type.name == 'MINION':
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        if len(owner.board) < 7:
            # Summon a copy
            copy = create_card(attacker.card_id, game)
            if copy:
                m = Minion(copy.data, game) if not isinstance(copy, Minion) else copy
                m.controller = owner
                owner.summon(m)
                
                # Attack enemy hero (simplified)
                opponent = game.get_opponent(owner)
                if opponent and opponent.hero:
                    game.deal_damage(opponent.hero, m.attack, m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
