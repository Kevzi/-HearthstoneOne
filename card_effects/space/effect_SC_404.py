"""Effect for Salvage the Bunker (SC_404).

Card Text: Summon two 2/2 Marines with <b>Taunt</b>.
Your next <b>Starship</b>
launch costs (2) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass