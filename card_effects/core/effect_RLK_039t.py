"""Effect for Grain Crate (RLK_039t).

Card Text: <b>Casts When Drawn</b>
Summon a 2/2 Undead Peasant.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass