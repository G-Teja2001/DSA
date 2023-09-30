def mergeSort(arr, start, end):
    if start < end:
        mid = start + (end - start)//2 #(start + end) // 2
    
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)

        merge(arr, start, mid, end)

def merge(arr, start, mid,end):
    temp = [0] * (end-start+1)
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    # Left arr
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    # Right Part
    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1
    # Copy
    for i in range(len(temp)):
        arr[start + i] = temp[i]

def merge(arr, start, mid, end):
    left_half = arr[start:mid + 1]
    right_half = arr[mid + 1:end+1]

    i = j = 0
    k = start

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

arr = [5, 4, 1, 3, 2]
mergeSort(arr, 0, 4)
print(arr)
