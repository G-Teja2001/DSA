def search(arr, n, target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == target:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= target and target <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1

arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
n = 9
target = 1
print(search(arr, n, target))