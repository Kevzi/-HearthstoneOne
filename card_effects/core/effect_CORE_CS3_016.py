"""CORE_CS3_016 - Reckoning: After an enemy minion deals 3 or more damage, destroy it."""

def on_damage_dealt(game, owner, secret, source=None, target=None, amount=0):
    if source and source.controller != owner and source.card_type.name == 'MINION' and amount >= 3:
        game.destroy(source)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
