"""GDB_875 - Spacerock Collector"""
def on_battlecry(game, player, card, target=None):
    # Your next Combo card costs (1) less.
    player.add_aura("next_combo_cost_reduction", 1)
