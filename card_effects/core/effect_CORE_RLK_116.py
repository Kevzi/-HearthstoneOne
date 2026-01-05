"""Effect for Necrotic Mortician (CORE_RLK_116).

Card Text: <b>Battlecry:</b> If a friendly Undead died after your
last turn, <b>Discover</b> an Unholy Rune card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass