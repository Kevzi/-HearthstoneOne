"""Effect for Wailing Rhapsody (JAM_018t4).

Card Text: Deal $3 damage to all minions. Summon
a 5/5 Demon.
<i>(Changes each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Summon effect
    # TODO: Implement summon logic for specific token
    pass