# Log(n)
def flipBits(A, B):
    count = 0
    while A or B:
        # Get LSB
        bitMask1 = A & 1
        bitMask2 = B & 1
        # Right Shift By 1
        A = A >> 1
        B = B >> 1
        # Increment Count
        if bitMask1 != bitMask2:
            count += 1
        
    return count

# Optimized Way
def flipBits2(A, B):
    res = A^B
    count = 0
    for i in range(64):
        if res & (1<<i) > 0:
            count += 1
    return count

print(flipBits(13, 9))