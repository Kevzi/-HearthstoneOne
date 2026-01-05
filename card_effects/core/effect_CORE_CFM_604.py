"""Effect for Greater Healing Potion (CORE_CFM_604).

Card Text: Restore #12 Health to a friendly character. Draw a card.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 12 card(s)
    player.draw(12)
    # Restore 12 Health
    if target:
        game.heal(target, 12, source)