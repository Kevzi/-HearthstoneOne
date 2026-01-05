"""Effect for Remorseless Winter (RLK_709).

Card Text: Deal $2 damage to all enemies. Draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 2, source)
    game.deal_damage(opponent.hero, 2, source)
    # Draw 2 card(s)
    player.draw(2)