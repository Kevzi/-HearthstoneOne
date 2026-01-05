"""Effect for Backup Tuning Fork (JAM_015t4).

Card Text: [x]<b>Battlecry:</b> <b>Discover</b>
a <b>Taunt</b> minion.
     <i>(Changes each turn.)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass