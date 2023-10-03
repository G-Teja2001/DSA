def findMin(arr):
    low = 0
    high = len(arr) - 1

    ans = float('inf')

    while low <= high:
        mid = (low+high)//2
        # mini optimization
        # Handling Sorted Arrays
        # i.e [1,2,3,4,5]
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
        # Left Sorted Arr
        if arr[low] <= arr[mid]:
            ans = min(arr[low], ans)
            low = mid + 1
        else: # Right Sorted Arr
            ans = min(arr[mid], ans)
            high = mid - 1
    return ans

print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([4, 5, 1, 2, 3]))