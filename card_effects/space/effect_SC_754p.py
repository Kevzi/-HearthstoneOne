"""Effect for Twin Blades (SC_754p).

Card Text: [x]Give a friendly minion and
your hero +$a1 Attack this
turn and <b>Divine Shield</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give keywords
    if target:
        target._divine_shield = True