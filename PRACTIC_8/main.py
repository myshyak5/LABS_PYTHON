import os
import csv
import random

filename = "example.csv"

def Read():
    with open(filename, 'r') as f:
        data = list(csv.reader(f))
    return data[0], data[1:]
def Show(out_type = "top", rows_count = 5, separator = ","):
    header, rows = Read()
    if out_type == "top":
        rows = rows[:rows_count]
    elif out_type == "bottom":
        rows = rows[-rows_count:]
    elif out_type == "random":
        rows = random.sample(rows, rows_count)
    print(*header, sep = separator)
    for row in rows:
        print(*row, sep = separator)
    if len(rows) < 5:
        print("Недостаточно строк.")
def Info():
    header, rows = Read()
    rows_count = len(rows)
    col_count = len(header)
    print(rows_count,"x",col_count, sep = "")
    column_stats = {col: {'count': 0, 'type': None} for col in header}
    for row in rows:
        for i, value in enumerate(row):
            if value:
                column_stats[header[i]]['count'] += 1
                if column_stats[header[i]]['type'] is None:
                    if value.isdigit():
                        column_stats[header[i]]['type'] = "int"
                    else:
                        column_stats[header[i]]['type'] = "string"
    for col, key in column_stats.items():
        print(f"{col} {key['count']} {key['type']}")
def DelNaN():
    header, rows = Read()
    new_rows = []
    for row in rows:
        add = True
        for value in row:
            if value == "":
                add = False
                break
        if add:
            new_rows.append(row)
    with open(filename, 'w', newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_rows)
def MakeDS():
    header, rows = Read()
    random.shuffle(rows)
    learn_data = rows[:int(len(rows) * 0.7)]
    test_data = rows[int(len(rows) * 0.7):]
    os.makedirs("workdata/Learning")
    os.makedirs("workdata/Testing")
    with open("workdata/Learning/train.csv", 'w', newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(learn_data)
    with open("workdata/Testing/test.csv", 'w', newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(test_data)   
if __name__ == "__main__":
    Show()
    Info()
    DelNaN()
    MakeDS()
