import requests
from collections import Counter


def main(url: str):
    response = requests.get(url)

    counter = Counter(response.text)

    with open('readme.md', 'w') as f:
        f.write('# Парс страницы www.python.org\n')
        f.write('| Символ | Количество |\n')
        f.write('|--------|------------|\n')
        for symbol, count in counter.items():
            f.write(f'| {symbol} | {count} |\n')


if __name__ == '__main__':
    main('http://www.python.org')
