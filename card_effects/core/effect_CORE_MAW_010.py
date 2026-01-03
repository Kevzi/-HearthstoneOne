"""CORE_MAW_010 - Motion Denied: After opponent plays 3 cards in a turn, deal 6 damage to enemy hero."""

def on_card_played(game, owner, secret, card=None, player=None):
    if player and player != owner:
        if hasattr(player, 'cards_played_this_turn') and player.cards_played_this_turn >= 3:
            game.deal_damage(player.hero, 6, secret)
            return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
