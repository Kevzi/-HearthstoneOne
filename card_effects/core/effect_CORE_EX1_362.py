"""Effect for Argent Protector (CORE_EX1_362).

Card Text: <b>Battlecry:</b> Give a friendly minion <b>Divine Shield</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give keywords
    if target:
        target._divine_shield = True