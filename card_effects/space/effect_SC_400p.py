"""Effect for Stimpack (SC_400p).

Card Text: [x]Summon a 2/2
Marine with <b>Taunt</b>.
Give your Terran
minions +2 Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass