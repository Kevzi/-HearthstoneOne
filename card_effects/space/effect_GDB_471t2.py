"""Effect for Tactical Crewmate (GDB_471t2).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Summon every
adjoining Crewmate.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass