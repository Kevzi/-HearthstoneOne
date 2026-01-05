"""Effect for Orbital Halo (GDB_439).

Card Text: Give a minion +1/+1 and <b>Divine Shield</b>. Costs (0) if you played an adjacent card this turn.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give keywords
    if target:
        target._divine_shield = True