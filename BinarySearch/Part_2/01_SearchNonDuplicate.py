def search(arr, n):
    if n == 1:
        return arr[0]
    
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]

        if mid%2 == 1:
            if arr[mid-1] == arr[mid]:
                low = mid + 1
            elif arr[mid+1] == arr[mid]:
                high = mid - 1
        else:
            if arr[mid+1] == arr[mid]:
                low = mid + 1
            elif arr[mid-1] == arr[mid]:
                high = mid - 1
    
    return -1
arr = [1,1,2,2,3,3,4,5,5,6,6]
n = len(arr)
print(search(arr, n))