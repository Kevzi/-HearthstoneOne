"""Effect for Gnome Muncher (RLK_720).

Card Text: [x]<b>Taunt</b>, <b>Lifesteal</b>
At the end of your turn,
attack the lowest Health
enemy.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 1 Health
    if target:
        game.heal(target, 1, source)