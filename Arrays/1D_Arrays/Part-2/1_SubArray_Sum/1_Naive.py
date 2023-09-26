nums = [2, 4, 6, 8, 10]
n = len(nums)

# O(n^3)
maxSubArrSum = -float('inf')
for i in range(0, n):
    start = i
    for j in range(i, n):
        end = j
        currSum= 0
        for k in range(start, end+1):
            currSum += nums[k]
        if currSum > maxSubArrSum:
            maxSubArrSum = currSum
print(maxSubArrSum)