nums = [2, 4, 6, 8, 10]
n = len(nums)

for i in range(0, n-1):
    for j in range(i+1, n):
        print(f'({nums[i]}, {nums[j]})', end='')
    print()