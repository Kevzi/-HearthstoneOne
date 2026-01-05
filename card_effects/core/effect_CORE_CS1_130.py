"""Effect for Holy Smite (CORE_CS1_130).

Card Text: Deal $3 damage
to a minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)