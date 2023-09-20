def isSortedArray(arr, i):
    if (len(arr)-1) == i:
        print(True)
        return
    if arr[i] > arr[i+1]:
        print(False)
        return
    isSortedArray(arr, i+1)

isSortedArray([1,2,3,4], 0)