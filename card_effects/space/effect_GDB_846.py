"""Effect for Exarch Naielle (GDB_846).

Card Text: <b>Battlecry:</b> Replace your
Hero Power with Tracking
<i>(<b>Discover</b> a card from your deck)</i>.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Discover effect
    # TODO: Implement discover with proper card pool
    pass