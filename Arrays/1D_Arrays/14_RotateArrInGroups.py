def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArrinGroups(arr, k):
    n = len(arr)
    
    numLoops = n//k if n//k == 0 else n//k + 1

    for i in range(numLoops):
        start = i * k
        end = min(i + k - 1, n - 1)
        reverse(arr, start, end)

arr = [1,2,3,4,5]
k = 3
rotateArrinGroups(arr, k)
print(arr)