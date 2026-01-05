"""Effect for Consume (SC_020).

Card Text: [x]Remove 1 Durability
from a friendly location
to restore #8 Health to
your hero.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)