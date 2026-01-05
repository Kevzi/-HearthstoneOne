"""Effect for Deathbringer Saurfang (RLK_082).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Return this to
your hand. It costs Health
instead of Mana.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)