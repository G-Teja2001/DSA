def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArrinGroups(arr, k):
    n = len(arr)
    
    for i in range(0, n, k):
        start = i
        end = min(i+k-1, n-1)
        reverse(arr, start, end)

arr = [1,2,3,4,5]
k = 3
rotateArrinGroups(arr, k)
print(arr)