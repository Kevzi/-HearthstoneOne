"""Effect for Shadow Word: Ruin (CORE_EX1_197).

Card Text: Destroy all minions with 5 or more Attack.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()