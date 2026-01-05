"""Effect for Amulet of Warding (VAC_959t07t).

Card Text: Deal $6 damage.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)