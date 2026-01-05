"""Effect for Spikeridged Steed (CORE_UNG_952).

Card Text: Give a minion +2/+6 and <b>Taunt</b>. When it dies, summon a Stegodon.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass