"""Effect for Entrée (VAC_533t).

Card Text: <b>Deathrattle:</b> Your opponent summons a minion from their deck.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass