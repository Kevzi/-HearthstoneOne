"""Effect for Angsty Rhapsody (JAM_018t).

Card Text: Deal $3 damage to all minions. Draw 3 cards.
<i>(Changes each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Draw 3 card(s)
    player.draw(3)