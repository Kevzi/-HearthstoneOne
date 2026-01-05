"""Effect for Grimmer Patron (VAC_464t26).

Card Text: At the end of your turn, summon a copy of this minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass