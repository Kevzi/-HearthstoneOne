"""Effect for Lift Off (SC_410).

Card Text: Draw 2 Terran cards. Summon a 2/1 <b>Starship Piece</b> with an effect when launched.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass