"""Effect for Chia Drake (TOY_801t).

Card Text: <b>Mini</b>
<b>Choose One -</b> Gain
<b>Spell Damage +1</b>; or
Draw a spell.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)