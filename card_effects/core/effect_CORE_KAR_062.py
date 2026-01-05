"""Effect for Netherspite Historian (CORE_KAR_062).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, <b>Discover</b>
a Dragon.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass