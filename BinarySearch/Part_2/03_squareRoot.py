def naive(n):
    ans = 0
    for i in range(n+1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans

print(naive(36))

def optimal(n):
    ans = 0
    low = 1
    high = n

    while low <= high:
        mid = (low + high)//2
        if pow(mid, 2) > n:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    return ans

print(optimal(34))