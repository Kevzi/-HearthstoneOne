"""Effect for Orbital Moon (GDB_475).

Card Text: Give a minion <b>Taunt</b> and <b>Lifesteal</b>. If you played an adjacent card this turn, also give it <b>Reborn</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Effect: Give a minion <b>Taunt</b> and <b>Lifesteal</b>. If you played an adjacent card this turn, also give it <b>Reborn</b>.
    # TODO: Implement
    pass