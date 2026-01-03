"""CORE_LOOT_101 - Explosive Runes: After opponent plays a minion, deal 6 damage to it and excess to hero."""

def on_minion_played(game, owner, secret, minion=None):
    if minion:
        damage = 6
        # Deal damage to minion
        minion_health = minion.health
        game.deal_damage(minion, damage, secret)
        
        # Excess goes to hero
        if damage > minion_health:
            excess = damage - minion_health
            game.deal_damage(minion.controller.hero, excess, secret)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
