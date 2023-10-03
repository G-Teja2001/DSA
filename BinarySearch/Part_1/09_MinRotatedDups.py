def minimum(arr):
    low = 0
    high = len(arr) - 1

    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2
        
        # Check if the left subarray is sorted
        if arr[low] < arr[mid]:
            ans = min(arr[low], ans)
            low = mid + 1

        # Check if the right subarray is sorted
        elif arr[mid] < arr[high]:
            ans = min(arr[mid], ans)
            high = mid - 1

        # Handle the case where arr[low], arr[mid], and arr[high] are equal
        else:
            ans = min(arr[low], ans)
            low += 1
            high -= 1

    return ans

print(minimum([4, 5, 6, 7, 0, 1, 2]))
print(minimum([4, 5, 1, 2, 3]))
print(minimum([1, 1, 1, 0, 1, 1, 1]))