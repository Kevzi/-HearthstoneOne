"""Effect for Giant's Dance (ETC_387c).

Card Text: In 4 turns, summon three 8/8 Giants <b>(Secretly)</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass