"""Effect for Dissonant Mood (ETC_379t).

Card Text: Give your hero +4 Attack this turn. Gain 2 Armor.
<i>(Swaps each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Gain 4 Armor
    player.hero.gain_armor(4)