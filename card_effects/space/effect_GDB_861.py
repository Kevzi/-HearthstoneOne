"""Effect for Stranded Spaceman (GDB_861).

Card Text: [x]<b>Battlecry:</b> The next
Draenei you play gains
+2 Health and <b>Rush</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)