"""Effect for Research Crewmate (GDB_471t6).

Card Text: [x]<b>Poisonous</b>
<b>Battlecry:</b> Summon every
adjoining Crewmate.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass