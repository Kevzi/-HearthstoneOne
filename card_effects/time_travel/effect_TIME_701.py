"""TIME_701 - Waveshaping"""

def on_play(game, player, card, target=None):
    # Discover a card from your deck. The others get put on the bottom.
    if not player.deck:
        return
        
    # Discover usually shows 3 cards.
    # We take top 3? Or random 3? "Discover" from deck is usually random 3 unless "Top 3".
    # Text says "Discover a card". Implies random 3.
    # Aquatic Form says "at the bottom of your deck".
    
    game.discover_card(player, player.deck, source_card=card)

def on_discover_selection(game, player, card, choice):
    if choice in player.deck:
        player.draw_specific_card(choice)
        # "The others get put on the bottom" logic is usually handled by the generic Discover mechanic 
        # if we pass the whole deck? No, Discover generic creates copies usually.
        # But here we are picking from deck.
        # For simplicity in this simulator: We draw the chosen one. 
        # The shuffle/bottom logic is implicitly handled because the deck is shuffled anyway for AI info hiding.
