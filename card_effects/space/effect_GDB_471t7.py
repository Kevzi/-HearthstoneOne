"""Effect for Medical Crewmate (GDB_471t7).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> Summon every
adjoining Crewmate.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass