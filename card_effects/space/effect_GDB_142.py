"""Effect for The Ceaseless Expanse (GDB_142).

Card Text: [x]Costs (1) less for each time
a card was drawn, played, or
destroyed. <b>Battlecry:</b> Destroy
all other minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)
    # Destroy target
    if target:
        target.destroy()