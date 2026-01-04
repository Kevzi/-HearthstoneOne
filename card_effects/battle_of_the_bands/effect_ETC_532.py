"""Effect for ETC_532 in BATTLE_OF_THE_BANDS"""

def on_play(game, source, target):
    player = source.controller
    # Get last 3 unique spells played
    played_ids = []
    for cid in reversed(player.spells_played_this_game):
        if cid != source.card_id and cid not in played_ids:
            played_ids.append(cid)
        if len(played_ids) >= 3:
            break
            
    if not played_ids:
        return
        
    options = [create_card(cid, player) for cid in played_ids]
    
    def on_choose(game, card):
        game.current_player.add_to_hand(card)
        
    game.initiate_discover(player, options, on_choose)