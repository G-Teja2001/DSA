nums = [-1, -2, -3]
n = len(nums)

# O(n)
maxSum = -float('inf')
currSum = 0
count = 0
negativeSum = -float('inf')

for i in range(0, n):
    currSum = currSum + nums[i]
    if currSum < 0:
        negativeSum = max(negativeSum, currSum)
        currSum = 0
        count += 1

    maxSum = max(maxSum, currSum)
if count == n:
    print(negativeSum)
else:
    print(maxSum)