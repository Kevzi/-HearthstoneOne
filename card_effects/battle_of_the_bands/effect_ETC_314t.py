"""Effect for Dissonant Pop (ETC_314t).

Card Text: Deal $6 damage to all minions. Summon
a 3/3 Popstar.
<i>(Swaps each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass