"""Effect for Pulsing Pumpkins (TOY_829hp3).

Card Text: [x]Deal $3 damage,
with crushing <i>brawn!</i>
My army shall be yours,
if my Head is <i>drawn!</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Draw 3 card(s)
    player.draw(3)