"""Effect for Vampiric Blood (CORE_RLK_051).

Card Text: [x]Give your hero +5 Health.
Spend 3 <b>Corpses</b> to gain
5 more and draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 5 card(s)
    player.draw(5)
    # Restore 5 Health
    if target:
        game.heal(target, 5, source)