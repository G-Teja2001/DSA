nums = [10, 8, 0, 0, 12, 0]
n = len(nums)
i = 0

for j in range(n):
    if nums[i] != 0:
        i += 1
    elif nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1

print(nums)