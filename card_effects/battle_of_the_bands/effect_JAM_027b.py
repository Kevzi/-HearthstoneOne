"""Effect for Poison Bloom! (JAM_027b).

Card Text: [x]Give a friendly minion
+2 Health and <b>Lifesteal</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Restore 2 Health
    if target:
        game.heal(target, 2, source)