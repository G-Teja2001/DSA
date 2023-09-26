arr = [-2, -1, 6, 8, 10]

def sortedSquaredArray(arr):
    result = [0 for _ in arr]

    for i in range(len(arr)):
        result[i] = arr[i] * arr[i]
    
    result.sort()
    return result

print(sortedSquaredArray(arr))