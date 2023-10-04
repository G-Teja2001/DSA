import math

def naive(piles, h):
    maxHrs = max(piles)
    for k in range(1, maxHrs+1):
        totalHrs = 0
        for i in piles:
            totalHrs += math.ceil(i/k)
        if totalHrs <= h:
            return k
    return -1


def isPossible(piles, k):
    totalHrs = 0
    for i in piles:
        totalHrs += math.ceil(i/k)
    return totalHrs
    
def optimal(piles, h):
    maxHrs = max(piles)
    low = 1
    high = maxHrs

    while low<=high:
        mid = (low + high)//2
        if isPossible(piles, mid) <= h:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans
