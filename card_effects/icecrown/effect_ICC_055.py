"""ICC_055 - Drain Soul"""
# Lifesteal handled by engine for the Spell source damage?
# Usually Spells with Lifesteal tag need the damage dealer to be the spell card.

def on_play(game, player, card, target=None):
    if target:
        game.deal_damage(target, 3, source=card)
