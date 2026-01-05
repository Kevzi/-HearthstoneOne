"""Effect for Bad Omen (GDB_124).

Card Text: In 2 turns, summon two 6/6 Demons with <b>Taunt</b>.
If you're building a <b>Starship</b>, summon them now.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass