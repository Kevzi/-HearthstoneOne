"""Effect for TIME_064 (Chrono-Lord Deios) in TIME_TRAVEL"""

def battlecry(game, source, target):
    """Aura: Your Battlecries, Deathrattles, Hero Power, and end of turn effects trigger twice."""
    # Register the doubling aura on the controller when played
    controller = source.controller
    if controller:
        if not hasattr(controller, 'deios_active'):
            controller.deios_active = 0
        controller.deios_active += 1
    
    # Store reference for cleanup
    source._deios_cleanup = lambda: _cleanup_deios(source)

def _cleanup_deios(source):
    """Clean up aura when minion leaves play."""
    if source.controller and hasattr(source.controller, 'deios_active'):
        source.controller.deios_active = max(0, source.controller.deios_active - 1)

def deathrattle(game, source):
    """Clean up the aura on death."""
    _cleanup_deios(source)

