arr = [3, 2, 3, 1]

res = 0
for i in arr:
    res = res ^ i

rightmost_set_bit = res & -res

element1 = 0
element2 = 0

for i in arr:
    if i & rightmost_set_bit != 0:
        element1 = element1 ^ i
    else:
        element2 = element2 ^ i

print([element1, element2])