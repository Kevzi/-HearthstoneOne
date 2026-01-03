"""CORE_EX1_287 - Counterspell: Counter opponent's spell."""

def on_spell_cast(game, owner, secret, spell=None, target=None):
    if spell:
        return True  # Spell is countered in game.py
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
