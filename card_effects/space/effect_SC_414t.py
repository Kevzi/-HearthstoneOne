"""Effect for Thor, Explosive Payload (SC_414t).

Card Text: [x]<b>Battlecry:</b> Deal 5 damage.
  Repeat at a random enemy  
for each <b>Starship</b> you've
launched this game.@ <i>(@)</i>
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Deal 5 damage to a random enemy
    import random
    targets = list(opponent.board) + [opponent.hero]
    if targets:
        game.deal_damage(random.choice(targets), 5, source)