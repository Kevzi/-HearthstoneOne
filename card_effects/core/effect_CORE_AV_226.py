"""CORE_AV_226 - Ice Trap: When opponent casts a spell, return it to their hand. Costs (1) more."""

def on_spell_cast(game, owner, secret, spell=None, target=None):
    if spell:
        # Return spell to hand, costs 1 more
        spell.cost += 1
        spell.controller.hand.append(spell)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
