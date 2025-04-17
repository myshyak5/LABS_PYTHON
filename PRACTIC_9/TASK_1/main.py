import numpy as np

matrix_rows = []
with open("matrix.txt", "r") as f:
    for row in f.readlines():
        row_ = [int(i) for i in row.split(',')]
        matrix_rows.append(row_)
matrix = np.array(matrix_rows)
sum_matrix = np.sum(matrix)
max_matrix = np.max(matrix)
min_matrix = np.min(matrix)

for row in matrix:
    print(row)
print(f"sum: {sum_matrix}")
print(f"max: {max_matrix}")
print(f"min: {min_matrix}")