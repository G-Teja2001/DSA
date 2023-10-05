def findKthPositive(vec, k) -> int:
    for i in range(len(vec)):
        if vec[i] <= k:
            k += 1
        else:
            break
    return k

arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))

