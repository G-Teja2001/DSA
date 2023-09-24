def rightRotateBy1(arr):
    n = len(arr)
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp

arr = [10, 2, 5, 4, 2]
rightRotateBy1(arr)
print(arr)





def rightRotateByK(arr, k):
    n = len(arr)
    k = k % n

    temp = [0] * n

    for i in range(k, n):
        temp[i] = arr[i - k]

    for i in range(k):
        temp[i] = arr[n - k + i]

    for i in range(n):
        arr[i] = temp[i]

arr = [10, 2, 5, 4, 2]
k = 3
rightRotateByK(arr, k)
print(arr)





def rightRotateByK(arr, k):
    n = len(arr)
    k = k % n
    
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [10, 2, 5, 4, 2]
k = 3
rightRotateByK(arr, k)
print(arr)