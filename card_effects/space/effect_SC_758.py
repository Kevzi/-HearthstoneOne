"""Effect for Colossus (SC_758).

Card Text: [x]<b>Battlecry:</b> Deal 1 damage
to all enemies, twice.
<i>(Improved by Protoss spells
you cast this game!)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 1 damage to all enemies
    for m in list(opponent.board):
        game.deal_damage(m, 1, source)
    game.deal_damage(opponent.hero, 1, source)