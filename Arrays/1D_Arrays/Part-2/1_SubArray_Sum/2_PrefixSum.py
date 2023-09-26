nums = [2, 4, 6, 8, 10]
n = len(nums)

# O(n^2, n)
maxSubArrSum = -float('inf')

prefixArr = [0] * n
for i in range(n):
    prefixArr[i] = nums[i] + prefixArr[i-1]

print(prefixArr)
for i in range(0, n):
    start = i
    for j in range(i, n):
        end = j
        currSum = prefixArr[end] - prefixArr[start-1] if start!=0 else prefixArr[end] 
        
        if currSum > maxSubArrSum:
            maxSubArrSum = currSum
print(maxSubArrSum)