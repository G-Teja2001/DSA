# BruteForce
nums = [34, 8, 10, 3]
maxDiff = 0
n = len(nums)
for i in range(n):
    for j in range(n):
        if nums[i] <= nums[j]:
            maxDiff = max(maxDiff, j-i)

print(maxDiff)

# Efficient Approach
lmin = [0] * n
rmax = [0] * n

lmin[0] = nums[0]
rmax[n - 1] = nums[n - 1]

for i in range(1, n):
    lmin[i] = min(lmin[i - 1], nums[i])

for i in range(n - 2, -1, -1):
    rmax[i] = max(rmax[i + 1], nums[i])

i = j = 0
maxDiff = -1

while i<n and j<n:
    if lmin[i] <= rmax[j]:
        maxDiff = max(maxDiff, j-i)
        j += 1
    else:
        i += 1

print(maxDiff)