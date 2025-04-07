import json

res_dict = {}
with open("ex_2.json", "r") as f:
    data = json.load(f)
for dicts in data:
    name = dicts["name"]
    phone = dicts["phoneNumber"]
    res_dict[name] = phone
print(res_dict)