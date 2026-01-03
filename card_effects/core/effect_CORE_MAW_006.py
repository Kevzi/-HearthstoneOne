"""CORE_MAW_006 - Objection!: When opponent plays a minion, Counter it."""

def on_minion_played(game, owner, secret, minion=None):
    if minion:
        # Counter means destroy it immediately before battlecry
        game.destroy(minion)
        return True
    return False

def on_play(game, player, card, target=None):
    player.secrets.append(card)
