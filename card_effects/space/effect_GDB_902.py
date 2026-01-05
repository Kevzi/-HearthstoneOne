"""Effect for Infiltrate (GDB_902).

Card Text: Choose a minion.
Deal $3 damage to all other minions.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)