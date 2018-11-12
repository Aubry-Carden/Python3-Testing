import json

updated = []

with open('words.json') as f:
    data = json.load(f)

    for item in data:
        item = item.upper()
        updated.append(item)

with open('words.json', "r+") as f:
    f.write(json.dumps(updated))
