arr = [0, 2, 1, 1]
def fun(arr):
    n = len(arr)
    low = 0
    mid = 0

    high = n-1

    while mid <= high:
        if arr[mid] == 0:
            swap(arr, mid, low)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            swap(arr, mid, high)
            high -= 1
    return arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

print(fun(arr))