"""Effect for Shield Slam (CORE_EX1_410).

Card Text: Deal 1 damage to a minion for each Armor you have.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)