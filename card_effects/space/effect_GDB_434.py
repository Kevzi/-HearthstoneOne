"""Effect for Bolide Behemoth (GDB_434).

Card Text: [x]<b>Battlecry:</b> Your Asteroids deal
1 more damage this game.
<b><b>Spellburst</b>:</b> Shuffle 3 of
them into your deck.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to target
    if target:
        game.deal_damage(target, 1, source)