"""Effect for Nostalgic Clown (TOY_341t).

Card Text: [x]<b>Mini</b>
<b>Battlecry:</b> If you've played a
higher Cost card while holding
this, deal 4 damage.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 4 damage to target
    if target:
        game.deal_damage(target, 4, source)