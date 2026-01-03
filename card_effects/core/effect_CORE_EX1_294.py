"""CORE_EX1_294 - Mirror Entity: Summon a copy of opponent's minion."""

def on_minion_played(game, owner, secret, minion=None):
    if minion and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        copy = create_card(minion.card_id, game)
        if copy:
            m = Minion(copy.data, game) if not isinstance(copy, Minion) else copy
            m.controller = owner
            owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
