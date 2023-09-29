arr = [1, 4, 20, 3, 10, 5]
targetSum = 33
def fun(arr, targetSum):
    for i in range(len(arr)):
        currSum = 0
        for j in range(i, len(arr)):
            currSum += arr[j]
            if currSum == targetSum:
                return i, j
    return -1

print(fun(arr, targetSum))