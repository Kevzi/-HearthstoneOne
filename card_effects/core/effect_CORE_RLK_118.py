"""Effect for Tomb Guardians (CORE_RLK_118).

Card Text: Summon two 2/2 Zombies with <b>Taunt</b>. Spend 4 <b>Corpses</b> to
give them <b>Reborn</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Summon effect
    # TODO: Implement summon logic for specific token
    pass