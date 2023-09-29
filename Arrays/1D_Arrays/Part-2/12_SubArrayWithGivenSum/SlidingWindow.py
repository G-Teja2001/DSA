"""
The idea is simple as we know that all the elements in subarray are positive so,
 If a subarray has sum greater than the given sum then there is no possibility that adding elements to the current subarray will be equal to the given sum. 
 So the Idea is to use a similar approach to a sliding window. 

Time Complexity: O(n)
Auxiliary Space: O(1). Since no extra space has been taken.
"""

arr = [1, 4, 20, 3, 10, 5]
targetSum = 33

def fun(arr, targetSum):
    start = 0
    end = 0
    currSum = 0
    
    while end < len(arr):
        currSum += arr[end]
        
        while currSum > targetSum:
            currSum -= arr[start]
            start += 1
        
        if currSum == targetSum:
            return start, end
        
        end += 1
    
    return -1

print(fun(arr, targetSum))