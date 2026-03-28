#!/usr/bin/env python3
"""lorem_gen — Generate placeholder text, data, and test fixtures.

Usage:
    lorem_gen.py text --words 50
    lorem_gen.py text --sentences 5
    lorem_gen.py text --paragraphs 3
    lorem_gen.py name --count 10
    lorem_gen.py email --count 5
    lorem_gen.py json --schema '{"name":"string","age":"int","email":"email"}'
    lorem_gen.py csv --cols "name,age,email" --rows 10
"""

import sys
import json
import random
import string
import argparse

LOREM = """Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt Neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur adipisci velit""".split()

FIRST_NAMES = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack', 'Kate', 'Leo', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rose', 'Sam', 'Tara', 'Uma', 'Victor', 'Wendy', 'Xavier', 'Yara', 'Zach']
LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Harris', 'Clark']
DOMAINS = ['example.com', 'test.org', 'demo.net', 'sample.io', 'mock.dev']
STREETS = ['Main St', 'Oak Ave', 'Pine Rd', 'Elm Dr', 'Cedar Ln', 'Maple Blvd', 'Park Way', 'Lake Dr']
CITIES = ['Springfield', 'Portland', 'Austin', 'Denver', 'Seattle', 'Boston', 'Miami', 'Chicago']


def gen_words(n):
    return ' '.join(random.choice(LOREM) for _ in range(n))

def gen_sentence():
    length = random.randint(6, 15)
    words = [random.choice(LOREM) for _ in range(length)]
    words[0] = words[0].capitalize()
    return ' '.join(words) + '.'

def gen_paragraph():
    return ' '.join(gen_sentence() for _ in range(random.randint(3, 7)))

def gen_name():
    return f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}'

def gen_email():
    first = random.choice(FIRST_NAMES).lower()
    last = random.choice(LAST_NAMES).lower()
    sep = random.choice(['.', '_', ''])
    return f'{first}{sep}{last}@{random.choice(DOMAINS)}'

def gen_phone():
    return f'+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}'

def gen_address():
    return f'{random.randint(1,9999)} {random.choice(STREETS)}, {random.choice(CITIES)}'

def gen_int(lo=1, hi=100):
    return random.randint(lo, hi)

def gen_float(lo=0.0, hi=100.0):
    return round(random.uniform(lo, hi), 2)

def gen_bool():
    return random.choice([True, False])

def gen_date():
    y = random.randint(2020, 2026)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return f'{y}-{m:02d}-{d:02d}'

def gen_url():
    return f'https://{random.choice(DOMAINS)}/{gen_words(2).replace(" ", "-").lower()}'

def gen_uuid():
    import uuid
    return str(uuid.uuid4())

GENERATORS = {
    'string': lambda: gen_words(random.randint(2, 5)),
    'text': lambda: gen_sentence(),
    'name': gen_name,
    'email': gen_email,
    'phone': gen_phone,
    'address': gen_address,
    'int': lambda: gen_int(),
    'float': lambda: gen_float(),
    'bool': gen_bool,
    'date': gen_date,
    'url': gen_url,
    'uuid': gen_uuid,
    'word': lambda: random.choice(LOREM),
}


def cmd_text(args):
    if args.paragraphs:
        for i in range(args.paragraphs):
            print(gen_paragraph())
            if i < args.paragraphs - 1:
                print()
    elif args.sentences:
        for _ in range(args.sentences):
            print(gen_sentence())
    else:
        print(gen_words(args.words))


def cmd_name(args):
    for _ in range(args.count):
        print(gen_name())

def cmd_email(args):
    for _ in range(args.count):
        print(gen_email())

def cmd_phone(args):
    for _ in range(args.count):
        print(gen_phone())


def cmd_json(args):
    schema = json.loads(args.schema)
    results = []
    for i in range(args.count):
        obj = {}
        for key, type_name in schema.items():
            gen = GENERATORS.get(type_name, GENERATORS['string'])
            obj[key] = gen()
        if args.id:
            obj = {'id': i + 1, **obj}
        results.append(obj)

    if args.count == 1 and not args.array:
        print(json.dumps(results[0], indent=2))
    else:
        print(json.dumps(results, indent=2))


def cmd_csv(args):
    import csv
    import io
    cols = [c.strip() for c in args.cols.split(',')]
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(cols)
    
    for _ in range(args.rows):
        row = []
        for col in cols:
            gen = GENERATORS.get(col.lower(), GENERATORS['string'])
            val = gen()
            row.append(val)
        writer.writerow(row)
    
    print(output.getvalue().strip())


def main():
    p = argparse.ArgumentParser(description='Placeholder data generator')
    sub = p.add_subparsers(dest='cmd', required=True)

    s = sub.add_parser('text', help='Generate lorem ipsum')
    s.add_argument('--words', type=int, default=50)
    s.add_argument('--sentences', type=int)
    s.add_argument('--paragraphs', type=int)
    s.set_defaults(func=cmd_text)

    s = sub.add_parser('name', help='Generate names')
    s.add_argument('--count', '-n', type=int, default=5)
    s.set_defaults(func=cmd_name)

    s = sub.add_parser('email', help='Generate emails')
    s.add_argument('--count', '-n', type=int, default=5)
    s.set_defaults(func=cmd_email)

    s = sub.add_parser('phone', help='Generate phone numbers')
    s.add_argument('--count', '-n', type=int, default=5)
    s.set_defaults(func=cmd_phone)

    s = sub.add_parser('json', help='Generate JSON from schema')
    s.add_argument('--schema', required=True, help='JSON schema like {"name":"name","age":"int"}')
    s.add_argument('--count', '-n', type=int, default=1)
    s.add_argument('--id', action='store_true', help='Add auto-increment id')
    s.add_argument('--array', action='store_true', help='Always output array')
    s.set_defaults(func=cmd_json)

    s = sub.add_parser('csv', help='Generate CSV data')
    s.add_argument('--cols', required=True, help='Column names (use generator names for auto-fill)')
    s.add_argument('--rows', type=int, default=10)
    s.set_defaults(func=cmd_csv)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
