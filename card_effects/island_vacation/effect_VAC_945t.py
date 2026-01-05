"""Effect for Ourobos, World Serpent (VAC_945t).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Give a minion
 in your hand "<b>Deathrattle:</b>
  Summon Ourobos."
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass