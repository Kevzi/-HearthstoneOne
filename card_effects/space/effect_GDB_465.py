"""Effect for Barrel Roll (GDB_465).

Card Text: [x]Deal $5 damage to an
undamaged character.
Costs (1) if you're
building a <b>Starship</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to target
    if target:
        game.deal_damage(target, 5, source)