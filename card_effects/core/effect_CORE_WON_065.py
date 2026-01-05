"""Effect for Ship's Chirurgeon (CORE_WON_065).

Card Text: After you summon a minion, give it +1 Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Restore 1 Health
    if target:
        game.heal(target, 1, source)