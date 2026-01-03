"""CORE_EX1_554 - Snake Trap: When one of your minions is attacked, summon three 1/1 Snakes."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    if defender and defender.controller == owner and defender.card_type.name == 'MINION':
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        # Summon 3 snakes
        for _ in range(3):
            if len(owner.board) >= 7:
                break
            snake = create_card("CS2_231", game)  # Wisp base
            if snake:
                m = Minion(snake.data, game)
                m.attack = 1
                m.health = 1
                m.max_health = 1
                m.name = "Snake"
                m.controller = owner
                owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
