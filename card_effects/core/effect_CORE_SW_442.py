"""Effect for Void Shard (CORE_SW_442).

Card Text: <b>Lifesteal</b>
Deal $4 damage.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 4 damage to target
    if target:
        game.deal_damage(target, 4, source)