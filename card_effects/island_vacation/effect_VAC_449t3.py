"""Effect for Carress, Cabaret Star (VAC_449t3).

Card Text: <b>Battlecry:</b> Draw 2 cards.
Restore 6 Health to
your hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Restore 2 Health
    if target:
        game.heal(target, 2, source)