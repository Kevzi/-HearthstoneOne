"""Effect for Black Hole (GDB_126).

Card Text: Destroy all minions except Demons.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()