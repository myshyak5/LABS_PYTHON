import json

add_data = {
    "id": 3,
    "total": 300.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 1,
            "price": 300.00
        }
    ]
}

with open("ex_3.json", "r") as f:
    data = json.load(f)
data["invoices"].append(add_data)
with open("ex_3_new.json", "w") as f:
    json.dump(data, f)