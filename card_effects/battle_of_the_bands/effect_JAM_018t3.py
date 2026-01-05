"""Effect for Emotional Rhapsody (JAM_018t3).

Card Text: [x]Deal $3 damage to all
minions. Give your hero
+5 Attack this turn.
<i>(Changes each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)