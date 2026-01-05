"""Effect for Ymirjar Deathbringer (RLK_Prologue_RLK_226).

Card Text: [x]<b>Taunt</b>. <b>Deathrattle:</b> Spend 3
<b>Corpses</b> to summon a 3/3
Risen Ymirjar with <b>Taunt</b>.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass