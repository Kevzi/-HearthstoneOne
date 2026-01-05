"""Effect for Canopic Jars (VAC_464t18).

Card Text: [x]Give your minions
"<b>Deathrattle:</b> Summon
a random <b>Legendary</b>
minion."
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass