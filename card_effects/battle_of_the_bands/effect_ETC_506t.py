"""Effect for Dissonant Disco (ETC_506t).

Card Text: <b>Discover</b> a 1-Cost minion. Summon it
with +5/+5.
<i>(Swaps each turn.)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Discover effect
    # TODO: Implement discover with proper card pool
    pass