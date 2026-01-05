"""Effect for Gorillabot A-3 (CORE_LOE_039).

Card Text: <b>Battlecry:</b> If you control another Mech, <b>Discover</b> a Mech.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass