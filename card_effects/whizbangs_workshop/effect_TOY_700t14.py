"""Effect for Quest Accepted! (TOY_700t14).

Card Text: Begin 3 Shaman <b>Quests</b>. Draw a Murloc and an <b>Overload</b> card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 3 card(s)
    player.draw(3)