"""Effect for Madame Lazul (CORE_DAL_729).

Card Text: [x]<b>Battlecry:</b> <b>Discover</b> a
copy of a card in your
opponent's hand.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass