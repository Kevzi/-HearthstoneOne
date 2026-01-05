"""Effect for Libram of Faith (GDB_139).

Card Text: Summon three
3/3 Draenei with <b>Divine Shield</b>. If this costs (0), give them <b>Rush</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Give keywords
    if target:
        target._rush = True
        target._divine_shield = True