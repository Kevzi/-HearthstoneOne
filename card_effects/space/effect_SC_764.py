"""SC_764 - Sentry: Lifesteal. Deathrattle: Your Protoss minions cost (1) less this game."""

def on_death(game, player, card):
    # Reduce cost of Protoss minions in hand and deck
    for c in player.hand + player.deck:
        if hasattr(c, 'data') and c.data and c.data.card_set == 'SPACE':
            if 'SC_' in c.card_id:
                c.cost = max(0, c.cost - 1)
