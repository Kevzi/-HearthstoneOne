"""Effect for Frost Strike (RLK_025).

Card Text: Deal $3 damage
to a minion. If that
kills it, <b>Discover</b> a
Frost Rune card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Discover effect
    # TODO: Implement discover with proper card pool
    pass