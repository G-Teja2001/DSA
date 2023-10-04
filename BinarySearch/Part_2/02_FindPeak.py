def naive(arr):
    n = len(arr)
    for i in range(n):
        if (i==0 or arr[i-1]<arr[i]) and (i==n-1 or arr[i] > arr[i+1]):
            return arr[i]

arr = [1,2,3,1]
print(naive(arr))

def optimized(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    
    low = 1
    high = n-1
    while low<=high:
        mid = (low + high)//2
        if arr[mid-1]<arr[mid] and arr[mid] > arr[mid+1]:
            return arr[mid]
        if arr[mid-1] < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

print(optimized(arr))
