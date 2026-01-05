"""Effect for Ancient's Melody (ETC_387b).

Card Text: In 2 turns, summon three 5/5 Ancients <b>(Secretly)</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass