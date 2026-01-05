"""Effect for Power Word: Shield (CORE_CS2_004).

Card Text: Give a minion +2 Health.
Draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)
    # Restore 2 Health
    if target:
        game.heal(target, 2, source)