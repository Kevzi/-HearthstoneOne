"""Effect for Divine Brew (VAC_916t2).

Card Text: Give a character <b>Divine Shield</b>. <i>(2 Drinks left!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give keywords
    if target:
        target._divine_shield = True