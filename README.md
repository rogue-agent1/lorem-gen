# lorem_gen

Generate placeholder text, mock data, and test fixtures. 13 data types.

## Usage

```bash
# Lorem ipsum text
python3 lorem_gen.py text --paragraphs 3
python3 lorem_gen.py text --sentences 5

# Mock data
python3 lorem_gen.py name -n 10
python3 lorem_gen.py email -n 5
python3 lorem_gen.py phone -n 5

# Generate JSON from schema
python3 lorem_gen.py json --schema '{"name":"name","age":"int","email":"email"}' -n 5 --id

# Generate CSV
python3 lorem_gen.py csv --cols "name,email,phone,date" --rows 20
```

## Data Types
string, text, name, email, phone, address, int, float, bool, date, url, uuid, word

## Zero dependencies. Single file. Python 3.8+.
