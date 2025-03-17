res = []
with open("input.txt", "r") as i_file:
    res = [int(i) for i in i_file.readlines()]
res = sorted(res, key = str)
with open("output.txt", "w") as o_file:
    for i in range(len(res)):
        o_file.write(str(res[i]))
        if (i != 9):
            o_file.write(" ")