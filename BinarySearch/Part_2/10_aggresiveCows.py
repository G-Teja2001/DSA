def naive(arr, k):
    arr.sort()
    maxi = -1
    for i in range(1, arr[-1] - arr[0] + 1):
        if isPossible(arr, k, i):
            ans = i
    
    return ans

def isPossible(arr, min_distance, k):
    count = 1
    prev = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - prev >= min_distance:
            count += 1
            prev = arr[i]
    
    return count >= k

print(naive([0, 3, 4, 7, 9, 10], 4))

def optimized(arr, k):
    arr.sort()
    low = 0
    high = arr[-1]

    while low <= high:
        mid = (low + high) // 2
        if isPossible(arr, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

print(optimized([0, 3, 4, 7, 9, 10], 4))