"""CORE_KAR_004 - Cat Trick: After opponent casts a spell, summon a 4/2 Panther with Stealth."""

def on_spell_cast(game, owner, secret, spell=None, target=None):
    if spell and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        panther = create_card("CS2_231", game)
        if panther:
            m = Minion(panther.data, game)
            m.attack = 4
            m.health = 2
            m.max_health = 2
            m.name = "Cat in a Hat"
            m._stealth = True
            m.controller = owner
            owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
