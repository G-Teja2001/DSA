import math

def naive(arr, threshold):
    for i in range(1, max(arr)+1):
        sum = 0
        for j in arr:
            sum += math.ceil(j/i)
        if sum <= threshold:
            return i

def isPossible(arr, threshold, num):
    sum = 0
    for j in arr:
        sum += math.ceil(j/num)
    return sum <= threshold

class Solution:
    def smallestDivisor(self, arr, threshold: int) -> int:
        low = 1
        high = max(arr)
        ans = -1

        while low<=high:
            mid = (low + high)//2

            if self.isPossible(arr, threshold, mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
    
    def isPossible(self, arr, threshold, num):
        sum = 0
        for j in arr:
            sum += math.ceil(j/num)
        return sum <= threshold
