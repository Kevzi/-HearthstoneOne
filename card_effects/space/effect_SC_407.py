"""Effect for Lock On (SC_407).

Card Text: Set a minion’s Health to 1. Your next <b>Starship</b>
launch costs (2) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)