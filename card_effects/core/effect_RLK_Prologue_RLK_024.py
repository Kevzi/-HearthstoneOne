"""Effect for Death Strike (RLK_Prologue_RLK_024).

Card Text: <b>Lifesteal</b>
Deal $6 damage
to a minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 6 damage to target
    if target:
        game.deal_damage(target, 6, source)