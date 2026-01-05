"""Effect for Big Game Hunter (CORE_EX1_005).

Card Text: [x]<b>Tradeable</b>
<b>Battlecry:</b> Destroy a minion
with 7 or more Attack.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()