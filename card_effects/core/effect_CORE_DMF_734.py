"""Effect for Greybough (CORE_DMF_734).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Give a random
friendly minion "<b>Deathrattle:</b>
Summon Greybough."
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass