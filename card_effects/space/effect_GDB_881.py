"""Effect for Pressure Points (GDB_881).

Card Text: Deal $3 damage to a minion. Reduce the Cost of <b>Combo</b> cards in your hand by (1).
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)