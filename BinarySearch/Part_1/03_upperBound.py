arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
x = 9

def linear(arr, x):
    n = len(arr)

    for i in range(n):
        if arr[i] > x:
            return i
    return n

print(linear(arr, x))

def binarySearch(arr, x):
    n = len(arr)
    low = 0
    high = n-1
    ans = n

    while low<=high:
        mid = (low + high)//2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print(binarySearch(arr, x))
