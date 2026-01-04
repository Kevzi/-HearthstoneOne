"""EDR_104 - Violet Spellwing"""
def on_deathrattle(game, minion):
    # Add an Arcane Missiles to your hand
    from simulator.factory import create_card
    missiles = create_card("EX1_277", game)
    if missiles:
        minion.controller.add_to_hand(missiles)
