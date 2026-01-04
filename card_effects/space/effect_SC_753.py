"""Effect for SC_753 (Photon Cannon) in SPACE"""

def on_play(game, source, target):
    """Deal 3 damage. If kills minion, Protoss minions cost (1) less this game."""
    if target is None:
        return
    
    initial_health = target.health
    game.deal_damage(target, 3, source)
    
    # Check if killed
    if target.health <= 0 or (hasattr(target, '_damage') and target._damage >= initial_health):
        # Reduce cost of Protoss minions in hand and deck
        player = source.controller
        for card in player.hand + player.deck:
            if hasattr(card, 'data') and card.data.card_set == "SPACE":
                if hasattr(card.data, 'races') and card.data.races and "MECHANICAL" in card.data.races:
                    card._cost = max(0, card._cost - 1)
