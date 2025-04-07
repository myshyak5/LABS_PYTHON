import json
import jsonschema

with open("error_ex_1.json", "r") as f:
    data = json.load(f)
with open("ex_1_schema.json", "r") as f:
    schema = json.load(f)
try:
    jsonschema.validate(instance = data, schema = schema)
    print("Файл прошел валидацию.")
except jsonschema.ValidationError as e:
    print(f"Файл не прошел валидацию: {e.message}")