"""EDR_491 - Archdruid of Thorns"""
def on_battlecry(game, player, card, target=None):
    # Gain the Deathrattles of your minions that died this turn.
    # We check the minions in graveyard that died THIS turn.
    died_this_turn = [m for m in player.graveyard if getattr(m, 'died_turn', -1) == game.turn_count]
    
    for m in died_this_turn:
        if m.has_deathrattle:
             # Add deathrattle to this minion
             card.add_deathrattle_from(m)
