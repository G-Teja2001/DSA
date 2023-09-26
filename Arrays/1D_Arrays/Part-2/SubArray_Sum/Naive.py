nums = [2, 4, 6, 8, 10]
n = len(nums)

# O(n^3)
for i in range(0, n):
    start = i
    for j in range(i, n):
        end = j
        for k in range(start, end+1):
            print(nums[k], end=' ')
        print()
    print()