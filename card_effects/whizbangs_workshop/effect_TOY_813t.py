"""Effect for Toy Captain Tarim (TOY_813t).

Card Text: [x]<b>Mini</b>
<b>Taunt</b>. <b>Battlecry:</b> Set a
minion's Attack and Health
to this minion's.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)