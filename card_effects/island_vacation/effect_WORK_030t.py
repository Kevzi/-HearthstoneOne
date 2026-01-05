"""Effect for Blackrock Brochure (WORK_030t).

Card Text: Deal $3 damage to a minion and $1 to
its neighbors.
<i>(Flips each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)