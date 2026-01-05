"""Effect for Lightshower Elemental (CORE_BAR_310).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Restore #8 Health
to all friendly characters.
"""

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    # Restore 8 Health to all friendly characters
    for m in player.board:
        game.heal(m, 8, source)
    game.heal(player.hero, 8, source)