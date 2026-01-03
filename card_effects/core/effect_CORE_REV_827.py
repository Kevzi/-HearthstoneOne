"""CORE_REV_827 - Sticky Situation: After opponent casts a spell, summon a 3/4 Spider with Stealth."""

def on_spell_cast(game, owner, secret, spell=None, target=None):
    if spell and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        spider = create_card("CS2_231", game)
        if spider:
            m = Minion(spider.data, game)
            m.attack = 3
            m.health = 4
            m.max_health = 4
            m.name = "Spider"
            m._stealth = True
            m.controller = owner
            owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
