from hearthstone.deckstrings import parse_deckstring
import sys

code = "AAECAa0GCMekBvvuBv/0Bpf8BryDB4KYB9yxB/GxBwuLowThpQbo+Qa8+gb6/Qbr/waPgAf5hAegkQeIlQcAAQP1swbHpAb3swbHpAbu3gbHpAYAAA=="

print(f"Decoding: {code}")
try:
    decoded = parse_deckstring(code)
    print("Raw decoded structure:")
    print(decoded)
    
    cards = decoded[0]
    heroes = decoded[1]
    format_type = decoded[2]
    
    print(f"\nCards (Count: {len(cards)}):")
    for dbf_id, count in cards:
        print(f"  ID: {dbf_id}, Count: {count}")
        
    print(f"\nHeroes: {heroes}")
    print(f"Format: {format_type}")
    
    # Check if there is a 4th element for sideboards in newer library versions
    if len(decoded) > 3:
        print(f"\nElement 4 (Sideboard?): {decoded[3]}")

except Exception as e:
    print(f"Error: {e}")
