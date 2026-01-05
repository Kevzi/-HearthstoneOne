"""Effect for Gorm the Worldeater (GDB_842).

Card Text: [x]<b>Dormant</b> for 5 turns. At the
end of your turn, destroy the
 minion to the right of this to
  awaken 1 turn sooner.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Destroy target
    if target:
        target.destroy()