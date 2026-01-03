"""CORE_SCH_706 - Plagiarize: At end of opponent's turn, add copies of cards they played to your hand."""

def on_turn_end(game, owner, secret):
    opponent = game.get_opponent(owner)
    if opponent and hasattr(opponent, 'cards_played_this_turn_list'):
        from simulator.factory import create_card
        
        for card_id in opponent.cards_played_this_turn_list:
            if len(owner.hand) < 10:
                copy = create_card(card_id, game)
                if copy:
                    owner.add_to_hand(copy)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
