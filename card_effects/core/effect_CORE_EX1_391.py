"""Effect for Slam (CORE_EX1_391).

Card Text: Deal $2 damage to a minion. If it survives, draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)
    # Draw 2 card(s)
    player.draw(2)