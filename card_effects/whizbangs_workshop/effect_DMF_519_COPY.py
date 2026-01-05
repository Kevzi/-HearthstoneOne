"""Effect for Prize Plunderer (DMF_519_COPY).

Card Text: [x]<b>Combo:</b> Deal 1 damage to
a minion for each other card
you've played this turn.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)