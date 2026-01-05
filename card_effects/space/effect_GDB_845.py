"""Effect for Laser Barrage (GDB_845).

Card Text: Deal $3 damage
to a minion. If you're building a <b>Starship</b>, also damage its neighbors.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)