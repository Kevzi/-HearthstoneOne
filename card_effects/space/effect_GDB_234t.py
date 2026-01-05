"""Effect for Replicating Spore (GDB_234t).

Card Text: Summon a random 5-Cost minion. Your future Replicating Spores summon it as well.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass