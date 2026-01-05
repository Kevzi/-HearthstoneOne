"""Effect for Mystified To'cha (GDB_440).

Card Text: [x]<b>Battlecry:</b> If the combined
Health of both heroes is
exactly 42, set your hero's
Health to 42.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 42 Health
    if target:
        game.heal(target, 42, source)