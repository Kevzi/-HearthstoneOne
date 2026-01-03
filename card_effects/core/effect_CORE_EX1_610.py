"""CORE_EX1_610 - Explosive Trap: When hero attacked, deal 2 damage to all enemies."""

def on_hero_attacked(game, owner, secret, attacker=None, defender=None):
    if defender and defender == owner.hero:
        opponent = game.get_opponent(owner)
        if opponent:
            for minion in list(opponent.board):
                game.deal_damage(minion, 2, secret)
            game.deal_damage(opponent.hero, 2, secret)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
