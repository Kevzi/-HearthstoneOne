"""Effect for Mountain Bear (CORE_AV_337).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Summon two
2/4 Cubs with <b>Taunt</b>.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass