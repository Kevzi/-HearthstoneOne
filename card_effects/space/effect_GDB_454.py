"""Effect for Overzealous Healer (GDB_454).

Card Text: <b>Deathrattle:</b> Restore #6 Health to the enemy hero. <b><b>Spellburst</b>:</b> <b>Silence</b> this minion.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Restore 6 Health
    if target:
        game.heal(target, 6, source)