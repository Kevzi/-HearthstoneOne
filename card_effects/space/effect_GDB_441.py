"""Effect for Anchorite (GDB_441).

Card Text: Whenever another minion is <b>Overhealed</b>, give it that much extra Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)