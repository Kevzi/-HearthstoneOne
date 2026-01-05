"""Effect for Helm Crewmate (GDB_471t4).

Card Text: [x]<b>Windfury</b>
<b>Battlecry:</b> Summon every
adjoining Crewmate.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass