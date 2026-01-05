"""Effect for Silvermoon Portal (CORE_KAR_077).

Card Text: Give a minion +2/+2. Summon a random
2-Cost minion.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass