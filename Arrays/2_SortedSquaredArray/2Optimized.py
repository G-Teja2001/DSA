arr = [-2,-1, 6, 8, 10]

def sortedSquaredArray(arr):
    n = len(arr)
    result = [0 for _ in arr]
    left, right = 0, n-1
    for i in reversed(range(len(arr))):
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] * arr[left]
            left += 1
        else:
            result[i] = arr[right] * arr[right]
            right -= 1
    return result

print(sortedSquaredArray(arr))