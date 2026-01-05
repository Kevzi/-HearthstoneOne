"""Effect for Concussive Shells (SC_411).

Card Text: Deal $2 damage and gain 2 Armor.
Your next <b>Starship</b>
launch costs (2) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)
    # Gain 2 Armor
    player.hero.gain_armor(2)