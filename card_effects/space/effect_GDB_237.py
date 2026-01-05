"""Effect for Alien Encounters (GDB_237).

Card Text: Summon two 2/4 Beasts with <b>Taunt</b>. Costs
(1) less for each card you <b><b>Discover</b>ed</b> this game.
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