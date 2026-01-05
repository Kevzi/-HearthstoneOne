"""Effect for Shield Block (CORE_EX1_606).

Card Text: Gain 5 Armor.
Draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 5 card(s)
    player.draw(5)
    # Gain 5 Armor
    player.hero.gain_armor(5)