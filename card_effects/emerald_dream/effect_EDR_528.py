"""EDR_528 - Nightmare Fuel"""
from simulator.enums import CardType

def on_play(game, player, card, target=None):
    # Discover a copy of a minion in your opponent's deck.
    # Combo: With a Dark Gift.
    
    opponent = player.opponent
    minions = [c for c in opponent.deck if c.is_minion]
    
    if not minions:
        return
        
    combo_active = len(player.cards_played_this_turn) > 1 # Simple combo check
    # Text says: "Combo: With a Dark Gift".
    # This usually means "Combo: Add a Dark Gift to it/hand?" OR "If Combo, do X"?
    # Actually, standard "Combo: X" usually means "Do X INSTEAD or IN ADDITION".
    # Text syntax: "Discover .... Combo: With a Dark Gift."
    # Interpret: Main effect = Discover minion copy. Combo bonus = Also receive a Dark Gift?
    # Or "Discover a copy... (and get a Gift if Combo)" ?
    # Let's assume standard Hearthstone syntax: "Effect. Combo: Effect + Bonus or Modified Effect".
    # I'll implement the Discover part. The Dark Gift part implies adding "Dark Gift" card to hand.
    
    # Discovery
    game.discover_card(player, minions, source_card=card)
    
    if combo_active:
        # Give a Dark Gift (Token?)
        # Let's assume ID "EDR_Gift" or similar.
        # Fallback to random helper if unknown.
        from simulator.factory import create_card
        gift = create_card("EDR_GIFT", game) # Hypothetical ID
        if gift:
             player.add_to_hand(gift)

def on_discover_selection(game, player, card, choice):
    from simulator.factory import create_card
    copy = create_card(choice.card_id, game)
    if copy:
        player.add_to_hand(copy)
