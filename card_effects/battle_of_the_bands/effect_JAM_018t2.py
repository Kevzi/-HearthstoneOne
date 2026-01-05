"""Effect for Resounding Rhapsody (JAM_018t2).

Card Text: Deal $3 damage to
all minions, twice.
<i>(Changes each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)