"""Effect for Mortal Coil (CORE_EX1_302).

Card Text: Deal $1 damage to a minion. If that kills it, draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)
    # Draw 1 card(s)
    player.draw(1)