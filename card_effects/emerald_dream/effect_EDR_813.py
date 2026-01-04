"""EDR_813 - Morbid Swarm"""
def on_play(game, player, card, target=None):
    # Choose One - Summon two 1/1 Ants; or Spend 2 Corpses to deal 4 damage to a minion.
    options = [
        {"name": "Summon Ants", "id": "SWARM_ANTS"},
        {"name": "Deal 4 (2 Corpses)", "id": "SWARM_DMG"}
    ]
    game.choose_option(player, options, source_card=card)

def on_option_selection(game, player, card, choice_id, target=None):
    if choice_id == "SWARM_ANTS":
        from simulator.factory import create_card
        for _ in range(2):
            ant = create_card("EDR_813t", game) # Token Ant
            player.summon(ant)
    elif choice_id == "SWARM_DMG":
        if player.corpses >= 2:
            player.corpses -= 2
            if target:
                game.deal_damage(target, 4, source=card)
