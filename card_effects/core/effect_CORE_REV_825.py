"""CORE_REV_825 - Double Cross: When opponent spends all their Mana, draw 2 cards."""

def on_turn_end(game, owner, secret):
    opponent = game.get_opponent(owner)
    if opponent and opponent.mana == 0:
        owner.draw(2)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
