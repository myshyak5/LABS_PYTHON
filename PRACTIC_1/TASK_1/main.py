nums = [int(input()) for i in range(3)]

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(f'Max: {nums[-1]}', f'Min: {nums[0]}', sep = '\n')