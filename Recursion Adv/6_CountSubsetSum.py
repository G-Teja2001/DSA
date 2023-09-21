def countSubSetsSum(arr, n, target_sum):
    # Base case: If n becomes 0, check if the target sum is reached
    if n == 0:
        return 1 if target_sum == 0 else 0
    
    # Include the current element in the subset
    include_current = countSubSetsSum(arr, n - 1, target_sum - arr[n - 1])
    
    # Exclude the current element from the subset
    exclude_current = countSubSetsSum(arr, n - 1, target_sum)
    
    # Return the sum of subsets count including and excluding the current element
    return include_current + exclude_current

arr = [10, 20, 15]
target_sum = 25
result = countSubSetsSum(arr, len(arr), target_sum)
print("Number of subsets with sum", target_sum, "is:", result)
