"""Effect for Murloc Tidecaller (CORE_EX1_509).

Card Text: Whenever you summon a Murloc, gain +1 Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass