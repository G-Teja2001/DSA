arr = [10, 2, 5, 4, 2]
def leftRotateLeftBy1(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp

    print(arr)

leftRotateLeftBy1(arr)

# Naive Solution
arr = [10, 2, 5, 4, 2]
def leftRotateLeftByK(arr, k):
    n = len(arr)
    k = k % n

    temp = [0] * n

    for i in range(k):
        temp[i] = arr[i]
    
    for i in range(k, n):
        arr[i-k] = arr[i]
    
    for i in range(n - k, len(arr)):
        arr[i] = temp[i-(n-k)]
    print(arr)

leftRotateLeftByK(arr, 3)


# Optimized Solution
# O(n, 1)
def leftRotateLeftByK(arr, k):
    n = len(arr)
    k = k % n
    
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n - 1)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [10, 2, 5, 4, 2]
k = 3
leftRotateLeftByK(arr, k)
print(arr)