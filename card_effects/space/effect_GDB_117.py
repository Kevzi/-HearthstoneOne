"""Effect for Dirdra, Rebel Captain (GDB_117).

Card Text: <b>Rush</b>. <b>Battlecry:</b> Shuffle all
8 Crewmates into your deck. <b>Deathrattle:</b> Draw
two Crewmates.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 8 card(s)
    player.draw(8)