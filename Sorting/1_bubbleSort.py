arr = [5, 4, 1, 3, 2]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(bubbleSort(arr))