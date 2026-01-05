"""Effect for Malignant Horror (CORE_RLK_745).

Card Text: [x]<b>Reborn</b>
At the end of your turn,
spend 4 <b>Corpses</b> to summon
a copy of this minion.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass