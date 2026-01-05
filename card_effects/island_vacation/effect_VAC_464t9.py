"""Effect for Looming Presence (VAC_464t9).

Card Text: Draw 2 cards. Gain 4 Armor.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Gain 2 Armor
    player.hero.gain_armor(2)