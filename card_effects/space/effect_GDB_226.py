"""Effect for Hostile Invader (GDB_226).

Card Text: <b>Battlecry, <b>Spellburst</b>, and Deathrattle:</b> Deal 2 damage to all other minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 2 damage to target
    if target:
        game.deal_damage(target, 2, source)