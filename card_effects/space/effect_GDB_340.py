"""Effect for Star Vulpera (GDB_340).

Card Text: [x]<b>Tradeable</b>
 <b>Battlecry:</b> Destroy an enemy 
<b>Starship</b> or <b>Starship Piece</b>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()