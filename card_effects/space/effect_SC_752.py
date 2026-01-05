"""Effect for Dark Templar (SC_752).

Card Text: [x]<b>Stealth</b>. <b>Battlecry:</b> Destroy
an enemy minion.
<i>Play another Templar to
merge into an Archon!</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()