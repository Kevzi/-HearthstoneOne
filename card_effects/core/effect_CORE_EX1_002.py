"""Effect for The Black Knight (CORE_EX1_002).

Card Text: <b>Tradeable</b>
 <b>Battlecry:</b> Destroy an  enemy minion with <b>Taunt</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()