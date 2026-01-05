"""Effect for Extraterrestrial Egg (GDB_840).

Card Text: [x]<b>Deathrattle:</b> Summon a
3/5 Beast that attacks the
lowest Health enemy.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass
    # Restore 3 Health
    if target:
        game.heal(target, 3, source)