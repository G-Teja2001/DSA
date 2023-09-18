n = 10
count = 0
while n:
    bitMask = n & 1
    if bitMask:
        count += 1
    n = n >> 1

print(count)