import json

data = json.load(open('data/cards.json', encoding='utf-8'))
secrets = [c for c in data if c.get('id', '').startswith('CORE_') and c.get('type') == 'SPELL' and 'SECRET' in c.get('mechanics', [])]

for c in secrets:
    text = c.get('text', '').replace('\n', ' ').replace('\r', '')[:100]
    print(f"{c['id']}: {c['name']}")
    print(f"  -> {text}")
    print()
