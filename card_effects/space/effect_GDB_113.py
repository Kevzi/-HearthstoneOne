"""Effect for Airlock Breach (GDB_113).

Card Text: [x]Summon a 5/5 Undead
with <b>Taunt</b> and give your
hero +5 Health. Spend
5 <b>Corpses</b> to do it again.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Restore 5 Health
    if target:
        game.heal(target, 5, source)