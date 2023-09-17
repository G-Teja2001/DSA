arr = [4, 5, 2, 8]
targetSum = 7

def twoNumSum(arr, targetSum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            print([arr[left], arr[right]])
            return [arr[left], arr[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    print([-1])
    return []
        
        

twoNumSum(arr, targetSum)