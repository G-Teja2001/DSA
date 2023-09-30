def countingSort(arr):
    maxRange = 0
    freq = {}

    for i in arr:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1
        if i > maxRange:
            maxRange = i
    
    i = 0
    for num in range(maxRange + 1):
        while freq.get(num):
            arr[i] = num
            i += 1
            freq[num] -= 1

    return arr

arr = [5, 4, 1, 3, 2]
countingSort(arr)
print(arr)
