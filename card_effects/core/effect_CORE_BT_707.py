"""CORE_BT_707 - Ambush: After opponent plays a minion, summon a 2/3 Ambusher with Poisonous."""

def on_minion_played(game, owner, secret, minion=None):
    if minion and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        # Create a 2/3 Poisonous Ambusher
        ambusher = create_card("CS2_231", game)  # Wisp base
        if ambusher:
            m = Minion(ambusher.data, game)
            m.attack = 2
            m.health = 3
            m.max_health = 3
            m.name = "Ambusher"
            m._poisonous = True
            m.controller = owner
            owner.summon(m)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
