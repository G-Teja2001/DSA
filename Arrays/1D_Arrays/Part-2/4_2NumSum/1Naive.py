arr = [4, 5, 2, 8]
targetSum = 7

def twoNumSum(arr, targetSum):
    for i in range(len(arr)-1):
        firstNum = arr[i]
        for j in range(i+1, len(arr)):
            secondNum = arr[j]
            if firstNum + secondNum == targetSum:
                print([firstNum, secondNum])
                return [firstNum, secondNum]
    print([-1])
    return []

twoNumSum(arr, targetSum)