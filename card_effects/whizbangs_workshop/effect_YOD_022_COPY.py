"""Effect for Risky Skipper (YOD_022_COPY).

Card Text: After you play a minion, deal 1 damage to all minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)