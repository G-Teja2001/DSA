# https://www.codingninjas.com/studio/problems/one-odd-occurring_4606074

n = 5
arr = [1, 2, 3, 2, 3]
# Output: 1

res = 0
for i in arr:
    res = res ^ i
print(res)