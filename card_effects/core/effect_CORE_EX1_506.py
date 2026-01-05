"""Effect for Murloc Tidehunter (CORE_EX1_506).

Card Text: <b>Battlecry:</b> Summon a 1/1 Murloc Scout.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass