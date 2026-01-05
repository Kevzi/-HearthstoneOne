"""Effect for Arkonite Revelation (GDB_852).

Card Text: Draw a card. If it's a spell, it costs (1) less.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)