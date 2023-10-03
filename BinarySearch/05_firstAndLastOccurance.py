def naive(arr, x):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first = i
                last = i
            else:
                last = i
    
    return first, last

arr = [5,7,7,8,8,10]
x = 8
print(naive(arr, x))

def first(arr, x):
    n = len(arr)

    low = 0
    high = n - 1
    ans = -1

    while low >= high:
        mid = (low + high)//2

        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return ans

def first(arr, x):
    n = len(arr)

    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return ans

def last(arr, x):
    n = len(arr)

    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return ans

print(first(arr, x))
print(last(arr, x))
