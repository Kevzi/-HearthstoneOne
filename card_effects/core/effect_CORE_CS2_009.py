"""Effect for Mark of the Wild (CORE_CS2_009).

Card Text: Give a minion <b>Taunt</b> and +2/+3.<i>
(+2 Attack/+3 Health)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)