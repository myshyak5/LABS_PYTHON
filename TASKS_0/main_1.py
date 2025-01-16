nums = []
symb = []
res = ""

while True:
    try:
        num = int(input())
        nums.append(num)
    except ValueError:
        break

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[j], nums[i] = nums[i], nums[j]

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        symb.append("=")
    else:
        symb.append("<")

for i in range(len(nums)):
    if i < (len(nums) - 1):
        res += f"{nums[i]} {symb[i]} "
    else:
        res += str(nums[i])

print(res)