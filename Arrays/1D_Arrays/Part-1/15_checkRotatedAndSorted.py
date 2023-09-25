def ascendingOrderRotatedAndSorted(arr):
    n = len(arr)
    pivotal_point = 0

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            pivotal_point += 1
    
    if arr[n-1] > arr[0]:
        pivotal_point += 1

    return pivotal_point <= 1

print(ascendingOrderRotatedAndSorted([1,2,3]))

def descendingOrderRotatedAndSorted(arr):
    n = len(arr)
    pivotal_point = 0

    for i in range(n-1):
        if arr[i] < arr[i+1]:
            pivotal_point += 1
    
    if arr[n-1] < arr[0]:
        pivotal_point += 1
    
    return pivotal_point <= 1

print(descendingOrderRotatedAndSorted([4, 2, 1, 9, 8, 6]))
