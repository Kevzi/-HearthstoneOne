"""Effect for Amulet of Critters (VAC_959t06t).

Card Text: Summon a
random 4-Cost minion
and give it <b>Taunt</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass