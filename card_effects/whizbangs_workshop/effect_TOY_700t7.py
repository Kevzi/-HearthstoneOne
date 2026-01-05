"""Effect for Deck of Discovery (TOY_700t7).

Card Text: Your deck is filled with cards that <b>Discover</b> Druid spells and minions.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass