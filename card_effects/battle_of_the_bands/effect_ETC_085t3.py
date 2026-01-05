"""Effect for Movement of Wrath (ETC_085t3).

Card Text: Deal $6 damage to
all characters.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)