"""Effect for SI:7 Agent (CORE_EX1_134).

Card Text: <b>Combo:</b> Deal 3 damage.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)