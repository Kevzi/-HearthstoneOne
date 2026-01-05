"""Effect for Parachute (VAC_933t).

Card Text: <b>Casts When Drawn</b>
Summon a 1/1 Pirate with <b>Charge</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass