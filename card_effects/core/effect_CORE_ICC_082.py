"""CORE_ICC_082 - Frozen Clone: After opponent plays a minion, add 2 copies to your hand."""

def on_minion_played(game, owner, secret, minion=None):
    if minion:
        from simulator.factory import create_card
        
        # Add 2 copies to hand
        for _ in range(2):
            if len(owner.hand) < 10:
                copy = create_card(minion.card_id, game)
                if copy:
                    owner.add_to_hand(copy)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
