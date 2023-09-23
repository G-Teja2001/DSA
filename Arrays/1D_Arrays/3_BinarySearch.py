nums = [1, 3, 5, 6, 7]
key = 6
def binarySearch(nums, key):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            left = mid + 1
        elif nums[mid] > key:
            right = mid - 1
    return -1

print(binarySearch(nums, key))

def recursiveBinary(nums, key, left, right):
    if left > right:
        return -1
    mid = (left + right)//2
    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return recursiveBinary(nums, key, mid+1, right)
    elif nums[mid] > key:
        return recursiveBinary(nums, key, left, mid-1)

print(recursiveBinary(nums, key, 0, len(nums)-1))