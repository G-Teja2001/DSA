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

print(flipBits(13, 9))