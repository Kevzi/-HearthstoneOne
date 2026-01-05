"""Effect for Pulsing Pumpkins (TOY_829hp).

Card Text: [x]Deal $3 damage,
with crushing <i>brawn!</i>
<b>Discover</b> an Undead,
to serve as your <i>pawn!</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 3 damage to target
    if target:
        game.deal_damage(target, 3, source)
    # Discover effect
    # TODO: Implement discover with proper card pool
    pass