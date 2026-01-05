"""Effect for Interstellar Researcher (GDB_728).

Card Text: <b>Battlecry and <b>Spellburst</b>:</b> Draw a Libram.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)