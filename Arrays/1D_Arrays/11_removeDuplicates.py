# If Array is Sorted!
nums = [1, 1, 2, 3, 3]

idx = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        pass
    else:
        nums[idx] = nums[i]
        idx += 1

for i in range(idx):
    print(nums[i], end=' ')
print()






# If Array isnt Sorted
# O(n, n)
nums = [3, 3, 5, 1, 1, 2, 4, 7]
numsSet = set()

for i in nums:
    numsSet.add(i)

nums = list(numsSet)
print('Set')
for i in range(len(nums)):
    print(nums[i], end=' ')
print()






# Order is preserved if we use def dict
# O(n, n)
from collections import defaultdict

nums = [3, 3, 5, 1, 1, 2, 4, 7]
numsDict = defaultdict(int)

for num in nums:
    numsDict[num] += 1

unique_nums = list(numsDict.keys())
print('Default Dict')
for num in unique_nums:
    print(num, end=' ')
print()






# O(nlogn, 1)
nums = [3, 3, 5, 1, 1, 2, 4, 7]
nums.sort()

idx = 1
print('Sort')
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        pass
    else:
        nums[idx] = nums[i]
        idx += 1

for i in range(idx):
    print(nums[i], end=' ')
