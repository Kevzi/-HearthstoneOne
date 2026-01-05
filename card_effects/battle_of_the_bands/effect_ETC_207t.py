"""Effect for Barrel of Monkeys (ETC_207t).

Card Text: Summon a 1/4 Monkey with <b>Taunt</b>.
<i>(2 Monkeys left!)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass