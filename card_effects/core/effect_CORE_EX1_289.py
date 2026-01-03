"""CORE_EX1_289 - Ice Barrier: When hero attacked, gain 8 Armor."""

def on_hero_attacked(game, owner, secret, attacker=None, defender=None):
    if defender and defender == owner.hero:
        owner.hero.armor += 8
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
