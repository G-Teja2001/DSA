def NthRoot(n: int, m: int) -> int:
    for i in range(1, m+1):
        p = pow(i, n)
        if p == m:
            return i
        elif p>m:
            break
    return -1

print(NthRoot(3, 27))

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m

    while low <= high:
        mid = (low + high)//2
        p = pow(mid, n)
        if p == m:
            return mid
        elif p > m:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(NthRoot(3, 27))

