"""Effect for Rustrot Viper (CORE_SW_072).

Card Text: [x]<b>Tradeable</b>
<b>Battlecry:</b> Destroy your
opponent's weapon.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()