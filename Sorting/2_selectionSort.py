arr = [5, 4, 1, 3, 2]

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        swap(arr, i, mini)
    return arr

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(selectionSort(arr))