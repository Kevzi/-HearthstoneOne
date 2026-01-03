"""SC_759 - Shield Battery: Gain 6 Armor. Your next Protoss spell costs (2) less."""

def on_play(game, player, card, target=None):
    # Gain 6 Armor
    player.hero.armor += 6
    
    # Next Protoss spell costs (2) less - simplified: give aura for one turn
    # This would require a more complex aura system to track
    # For now, just gain the armor
    pass
