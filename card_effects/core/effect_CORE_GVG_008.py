"""Effect for Lightbomb (CORE_GVG_008).

Card Text: Deal damage to each minion equal to its Attack.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)