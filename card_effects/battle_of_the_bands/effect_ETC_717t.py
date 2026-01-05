"""Effect for Dissonant Hip Hop (ETC_717t).

Card Text: Deal $3 damage. Give your weapon +1 Attack.
<i>(Swaps each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)