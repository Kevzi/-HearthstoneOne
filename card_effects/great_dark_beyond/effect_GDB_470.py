"""GDB_470 - Exarch Maladaar"""
def on_battlecry(game, player, card, target=None):
    # The next card you play this turn costs Corpses instead of Mana.
    player.add_aura("next_card_costs_corpses", True, duration="TURN")
