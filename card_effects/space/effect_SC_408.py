"""Effect for Ghost (SC_408).

Card Text: [x]<b>Stealth</b>. <b>Battlecry:</b> If you're
building a <b>Starship</b>, destroy
the lowest-Cost card in your
opponent's hand.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()