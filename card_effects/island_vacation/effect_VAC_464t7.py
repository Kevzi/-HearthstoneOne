"""Effect for Holy Book (VAC_464t7).

Card Text: <b>Silence</b> and destroy a minion. Summon a 10/10 copy of it.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Destroy target
    if target:
        target.destroy()