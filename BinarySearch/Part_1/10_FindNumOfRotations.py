def rotations(arr):
    low = 0
    high = len(arr) - 1

    ans = float('inf')
    index = -1

    while low <= high:
        mid = (low+high)//2

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = min(arr[low], ans)
            low = mid + 1
        else:
            if arr[mid] < ans:
                index = mid
                ans = min(arr[low], ans)
            high = mid - 1
    return index

print(rotations([4, 5, 6, 7, 0, 1, 2]))
print(rotations([4, 5, 1, 2, 3]))