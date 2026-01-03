"""SC_783 - Void Ray: Rush, Divine Shield. Battlecry: If this costs (0), gain +2/+2."""

def on_play(game, player, card, target=None):
    # Check if card cost 0 when played
    if card.cost == 0:
        card.attack += 2
        card.health += 2
        card.max_health += 2
