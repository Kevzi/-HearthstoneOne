import json

TARGETS = ["Nightmare Lord Xavius"]

with open('data/cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for t in TARGETS:
    for card in cards:
        if t in card.get('name', ''):
            print(f"--- {card['name']} ---")
            print(f"ID: {card['id']}")
            print(f"Set: {card.get('set')}")
            print(f"Text: {card.get('text')}")
