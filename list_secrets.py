import json

data = json.load(open('data/cards.json', encoding='utf-8'))
secrets = [c for c in data if c.get('type') == 'SPELL' and 'SECRET' in c.get('mechanics', []) and c.get('collectible')]
print(f'Total secrets: {len(secrets)}')

# Group by class
by_class = {}
for s in secrets:
    cls = s.get('cardClass', 'NEUTRAL')
    if cls not in by_class:
        by_class[cls] = []
    by_class[cls].append(s)

for cls in sorted(by_class.keys()):
    print(f"\n=== {cls} ({len(by_class[cls])}) ===")
    for c in by_class[cls]:
        print(f"  {c['id']}: {c['name']} ({c.get('set', 'UNKNOWN')})")
