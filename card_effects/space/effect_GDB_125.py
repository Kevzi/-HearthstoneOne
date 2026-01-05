"""Effect for Healthstone (GDB_125).

Card Text: <b>Tradeable</b>
Restore all damage your hero has taken this turn.@
<i>(@)</i>
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)