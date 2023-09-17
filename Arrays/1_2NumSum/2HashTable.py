arr = [4, 5, 2, 8]
targetSum = 7

def twoNumSum(arr, targetSum):
    nums = {}
    for num in arr:
        match = targetSum - num
        if match in nums:
            print([match, num])
            return [match, num]
        else:
            nums[num] = True
    print([-1])
    return []

twoNumSum(arr, targetSum)