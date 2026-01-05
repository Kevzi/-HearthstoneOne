"""Effect for Barak Kodobane (CORE_BAR_551).

Card Text: [x]<b>Battlecry:</b> Draw a 1, 2,
  and 3-Cost spell.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)