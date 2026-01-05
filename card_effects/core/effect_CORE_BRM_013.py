"""Effect for Quick Shot (CORE_BRM_013).

Card Text: Deal $3 damage.
If your hand is empty, draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Draw 3 card(s)
    player.draw(3)