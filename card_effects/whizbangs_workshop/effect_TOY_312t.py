"""Effect for Nostalgic Gnome (TOY_312t).

Card Text: [x]<b>Mini</b>
<b>Rush</b>. After this minion deals
exact lethal damage on your
turn, draw a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)
    # Draw 1 card(s)
    player.draw(1)