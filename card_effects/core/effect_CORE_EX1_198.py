"""Effect for Natalie Seline (CORE_EX1_198).

Card Text: <b>Battlecry:</b> Destroy a minion and gain its Health.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)
    # Destroy target
    if target:
        target.destroy()