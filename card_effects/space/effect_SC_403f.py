"""Effect for Medivac (SC_403f).

Card Text: [x]<b>Starship Piece</b>
When this is launched,
summon two 2/2 Marines
with <b>Taunt</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass