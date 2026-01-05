"""Effect for Clay Matriarch (TOY_380t).

Card Text: [x]<b>Mini</b>
<b>Taunt</b>. <b>Deathrattle:</b> Summon
a 4/4 Whelp with <b>Elusive</b>.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass