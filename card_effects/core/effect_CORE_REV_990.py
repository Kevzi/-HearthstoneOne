"""Effect for Sanguine Depths (CORE_REV_990).

Card Text: [x]Deal 1 damage to a 
minion and give it 
+2 Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)