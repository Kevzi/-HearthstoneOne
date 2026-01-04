import json

def list_sets():
    try:
        with open('data/cards.json', 'r', encoding='utf-8') as f:
            cards = json.load(f)
            
        sets = set()
        for c in cards:
            if 'set' in c:
                sets.add(c['set'])
                
        print("Sets found in DB:")
        for s in sorted(list(sets)):
            print(f"- {s}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_sets()
