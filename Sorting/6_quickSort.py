def quickSort(arr, start, end):
    if start < end:
        partitionIdx = partition(arr, start, end)
        quickSort(arr, start, partitionIdx - 1)
        quickSort(arr, partitionIdx + 1, end)

def partition(arr, start, end):
    pivot = end
    i = start - 1
    
    for j in range(start, end):
        if arr[j] <= arr[pivot]:
            i += 1
            swap(arr, i, j)
    i += 1
    swap(arr, i, pivot)
    return i

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

arr = [5, 4, 1, 3, 2]
quickSort(arr, 0, 4)
print(arr)