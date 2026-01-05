"""Effect for Gnomish Army Knife (VAC_464t15).

Card Text: [x]Give a minion <b>Rush</b>,
<b>Windfury</b>, <b>Divine Shield</b>,
<b>Lifesteal</b>, <b>Poisonous</b>,
<b>Taunt</b>, and <b>Stealth</b>.
"""

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Give keywords
    if target:
        target._taunt = True
        target._rush = True
        target._divine_shield = True