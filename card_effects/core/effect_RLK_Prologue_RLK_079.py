"""Effect for Noxious Cadaver (RLK_Prologue_RLK_079).

Card Text: [x]<b>Battlecry</b>: Deal 2 damage
to an enemy and your hero.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)