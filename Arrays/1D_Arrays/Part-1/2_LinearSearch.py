def linearSearch(nums, key):
    for i in range(len(nums)):
        if key == nums[i]:
            return i
    return -1

print(linearSearch([1,2,3,4,5], 5))