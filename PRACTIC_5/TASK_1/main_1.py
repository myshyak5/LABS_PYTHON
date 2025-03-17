prod = 1
with open("input.txt", "r") as i_file:
    i_file = i_file.readline()
    for i in i_file.split():
        prod *= int(i)
with open("output.txt", "w") as o_file:
    o_file.write(str(prod))