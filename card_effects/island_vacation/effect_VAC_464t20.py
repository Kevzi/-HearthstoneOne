"""Effect for Banana Split (VAC_464t20).

Card Text: Give a friendly minion +2/+2. Summon two copies of it.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass