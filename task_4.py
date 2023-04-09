import json
from datetime import datetime


def update_json(data):
    if isinstance(data, dict):
        for key in data:
            if key == 'updated':
                data[key] = datetime.now().isoformat()
            else:
                update_json(data[key])
    elif isinstance(data, list):
        for item in data:
            update_json(item)


def main(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)

    update_json(data)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main('ex.json')

# для верхнего уровня
# for item in data:
#     if 'updated' in item:
#         item['updated'] = datetime.utcnow().isoformat()
