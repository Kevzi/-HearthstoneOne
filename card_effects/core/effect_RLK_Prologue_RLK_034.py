"""Effect for Heart Strike (RLK_Prologue_RLK_034).

Card Text: Deal $3 damage to
a minion. If that kills it, gain a <b>Corpse</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)