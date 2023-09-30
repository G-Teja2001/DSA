arr = [5, 4, 1, 3, 2]

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j>0 and arr[j] < arr[j-1]:
            swap(arr, j, j-1)
            j -= 1
        
    return arr

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(insertionSort(arr))