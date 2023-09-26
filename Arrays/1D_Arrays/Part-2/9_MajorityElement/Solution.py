arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 1, 1]

def fun(arr):
    element = None
    count = 0

    for i in range(len(arr)):
        if count == 0:
            element = arr[i]
            count += 1
        elif element == arr[i]:
            count += 1
        else:
            count -= 1

    count = 0

    for i in arr:
        if i == element:
            count += 1
    if count > len(arr)//2:
        return element
    return -1
    
print(fun(arr))