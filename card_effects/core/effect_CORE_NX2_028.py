"""Effect for Hookfist-3000 (CORE_NX2_028).

Card Text: After your hero attacks, gain 4 Armor and
draw a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 4 card(s)
    player.draw(4)
    # Gain 4 Armor
    player.hero.gain_armor(4)