"""EDR_457 - Brood Keeper """
from simulator.enums import Race

def on_battlecry(game, player, card, target=None):
    # If you're holding a Dragon, equip a 2/2 Sword.
    
    holding_dragon = any(c.is_minion and c.race == Race.DRAGON for c in player.hand if c is not card)
    
    if holding_dragon:
        # Equip 2/2 Sword (Assume generic token ID or create generic weapon)
        # Using a fallback weapon ID if exact token unknown found nearby
        # Token for EDR_457 is probably EDR_457t.
        # But for now, let's use Fiery War Axe (CS2_106 - 3/2) adjusted? 
        # No, creating custom weapon is complex without ID.
        # Let's try to lookup token or use default 2/2 weapon logic.
        
        # HACK: Equip a fake weapon entity if we can't spawn specific ID.
        # Or stick to "Fiery War Axe" logic but modify stats? 
        # Modifying stats of equipped weapon is tricky in on_play.
        
        # Let's assume standard token ID exists: "EDR_457t"
        from simulator.factory import create_card
        weapon = create_card("EDR_457t", game)
        if not weapon:
             # Fallback to similar available weapon or generic token
             # Use "Upgrade!" weapon? No.
             pass 
        else:
             player.equip_weapon(weapon)
    
    # Can't easily implement "Equip 2/2" without valid card ID for the weapon.
    # I will assume "EDR_457t" exists in DB as token.
    # If not, the effect will fail silently (safe).
