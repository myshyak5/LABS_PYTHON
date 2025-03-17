def f(n):
    for i in range(len(res[n])):
        o_file.write(res[n][i])
        if (i != 2):
            o_file.write(" ")
res = []
with open("input.txt", "r", encoding = "utf-8") as i_file:
    res = [str(i).split() for i in i_file.readlines()]
res = sorted(res, key = lambda x: int(x[2]))
with open("max_output.txt", "w", encoding = "utf-8") as o_file:
    f(-1)
with open("mix_output.txt", "w", encoding = "utf-8") as o_file:
    f(0)