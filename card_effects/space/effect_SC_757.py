"""Effect for SC_757 (Hallucination) in SPACE"""

def on_play(game, source, target):
    """Summon a copy of a friendly Protoss minion. It takes double damage."""
    if target is None:
        return
    
    player = source.controller
    
    # Create a copy of the target
    copy = game.summon_copy(target, player)
    
    if copy:
        # Mark the copy as taking double damage
        if not hasattr(copy, '_hallucination'):
            copy._hallucination = True
            # Attach damage modifier
            original_take_damage = copy.take_damage
            def take_double_damage(amount):
                return original_take_damage(amount * 2)
            copy.take_damage = take_double_damage
