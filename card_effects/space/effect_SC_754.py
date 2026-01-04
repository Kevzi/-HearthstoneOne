"""Effect for SC_754 (Artanis) in SPACE - Hero Card"""

def battlecry(game, source, target):
    """Battlecry: Summon two 3/4 Zealots with Charge. Protoss minions cost (2) less."""
    player = source.controller
    
    # Summon two Zealots
    for _ in range(2):
        zealot = game.summon_token(player, 'SC_754t', -1)
        if zealot:
            zealot._charge = True
    
    # Reduce cost of Protoss minions in hand and deck by 2
    for card in player.hand + player.deck:
        if hasattr(card, 'data') and card.data.card_set == "SPACE":
            if hasattr(card.data, 'races') and card.data.races and "MECHANICAL" in card.data.races:
                card._cost = max(0, card._cost - 2)
