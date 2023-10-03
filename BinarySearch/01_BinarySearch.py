arr = [1, 3, 5, 6, 7]
target = 6

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return -1

print(binarySearch(arr, target))

def recursiveBinary(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursiveBinary(arr, target, mid+1, high)
    elif arr[mid] > target:
        return recursiveBinary(arr, target, low, mid-1)

print(recursiveBinary(arr, target, 0, len(arr)-1))