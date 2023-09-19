n = 14
currCount = 0
maxCount = 0

while n:
    bitMask = n & 1
    if bitMask:
        currCount += 1
    else:
        maxCount = max(currCount, maxCount)
        currCount = 0
    n = n >> 1
maxCount = max(currCount, maxCount)
print(maxCount)