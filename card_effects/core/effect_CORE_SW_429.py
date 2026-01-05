"""Effect for Best in Shell (CORE_SW_429).

Card Text: [x]<b>Tradeable</b>
Summon two 2/7
 Turtles with <b>Taunt</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass