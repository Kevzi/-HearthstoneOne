"""DMF_511 - Foxy Fraud"""

def on_battlecry(game, player, card, target=None):
    # Your next Combo card this turn costs (2) less.
    player.add_aura("next_combo_cost_reduction", 2)
    # The aura system needs to handle 'combo' tag check.
    # Assuming simulator has robust aura/cost calc, this tag triggers it.
    # If not, we might need a manual "on_card_draw_cost_calc" or similar, 
    # but generic cost reduction is standard.
