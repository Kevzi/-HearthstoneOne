"""Effect for Celestial Aura (GDB_140).

Card Text: While you have exactly 1 minion in play, its Attack and Health are 10. Lasts 3 turns.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)