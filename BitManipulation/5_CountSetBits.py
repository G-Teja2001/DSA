n = 10
count = 0
# O(Logn)
while n:
    bitMask = n & 1
    if bitMask:
        count += 1
    n = n >> 1

print(count)

# O(SetBits) -> maxSetBits -> O(logn)
# Optimized Way is to turn of the set bits for some cases.. ot for 7 or 15 like nums its same as the above one.
n = 10
count = 0
while n:
    n = n & (n-1)
    count += 1

print(count)

# O(SetBits) -> maxSetBits -> O(logn)
n = 10
print(bin(n).count('1'))


# O(1)
count = 0
for i in range(64):
    if n & (1<<i) > 0:
        count += 1
print(count)