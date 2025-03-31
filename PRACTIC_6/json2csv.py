import json
import sys
import os

j_filename = sys.argv[1]
data = []
with open(j_filename, 'r', encoding = "utf-8") as f:
    j_data = json.load(f)
    name = list(j_data.keys())[0]
    if isinstance(j_data[name], list):
        data = j_data[name]
csv_filename = f"{name}.csv"
with open(csv_filename, 'w', encoding = "utf-8") as f:
    headers = data[0].keys()
    f.write(','.join(headers) + '\n')
    for elem in data:
        row = ','.join(str(elem[key]) for key in headers)
        f.write(f"{row}\n")