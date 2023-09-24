def checkRotatedAndSorted(arr):
    n = len(arr)
    pivotal_point = 0
    if arr[n - 1] <= arr[0]:
        for i in range(n - 1):
            if arr[i + 1]  < arr[i]:
                pivotal_point += 1
        if pivotal_point <= 1:
            return True
    
    elif arr[n - 1] > arr[0]:
        for i in range(n - 1):
            if arr[i + 1] > arr[i]:
                pivotal_point += 1
        if pivotal_point == 1:
            return True
    
    return False

print(checkRotatedAndSorted([4, 3, 2, 1]))