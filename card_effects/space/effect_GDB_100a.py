"""Effect for Emergency Repairs (GDB_100a).

Card Text: Gain Armor equal
to the <b>Starship's</b> Health, twice.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)
    # Gain 1 Armor
    player.hero.gain_armor(1)