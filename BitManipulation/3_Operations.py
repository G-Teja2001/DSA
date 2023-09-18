def getIthBit(n, i):
    bitMask = 1 << i
    if n & bitMask:
        return 1
    else:
        return 0

def setIthBit(n, i):
    bitMask = 1 << i
    return n | bitMask

def clearIthBit(n, i):
    bitMask = ~(1<<i)
    return n & bitMask

def updateIthBit(n, i, newBit):
    if newBit:
        return clearIthBit(n, i)
    return setIthBit(n, i)

def updateIthBit2(n, i, newBit):
    n = clearIthBit(n, i)
    bitMask = newBit << i

    return n | bitMask

def clearLastIthBits(n, i):
    bitMask = (~0) << i
    return n & bitMask

def setLastIthBits(n, i):
    bitMask = (1 << i) - 1
    return n | bitMask

def clearRangeOfBits(n, i, j):
    a = ~0 << j
    b = (1 << (i-1)) - 1
    bitMask = a | b
    return n & bitMask

print(getIthBit(7, 2))
print(setIthBit(10, 2))
print(clearIthBit(7, 2))
print(updateIthBit2(10, 2, 1))
print(clearLastIthBits(15, 3))
print(setLastIthBits(8, 2))
print(clearRangeOfBits(189, 3, 5))
