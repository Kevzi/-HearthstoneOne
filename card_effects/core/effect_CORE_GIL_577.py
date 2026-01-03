"""CORE_GIL_577 - Rat Trap: After opponent plays 3 cards in a turn, summon a 6/6 Rat."""

# This needs tracking of cards played by opponent per turn
def on_card_played(game, owner, secret, card=None, player=None):
    if player and player != owner:
        # Check if opponent has played 3 cards this turn
        if hasattr(player, 'cards_played_this_turn') and player.cards_played_this_turn >= 3:
            if len(owner.board) < 7:
                from simulator.factory import create_card
                from simulator.entities import Minion
                
                rat = create_card("CS2_231", game)
                if rat:
                    m = Minion(rat.data, game)
                    m.attack = 6
                    m.health = 6
                    m.max_health = 6
                    m.name = "Giant Rat"
                    m.controller = owner
                    owner.summon(m)
            return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
