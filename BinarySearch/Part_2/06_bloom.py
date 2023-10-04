def isPossible(arr, day, m, k):
    ans = 0
    count = 0
    for i in arr:
        if i <= day:
            count += 1
        else:
            ans = count//k
            count = 0
    ans += count//k
    return ans >= m

def naive(arr, m, k):
    if len(arr) < m*k:
        return -1
    
    mini = min(arr)
    maxi = max(arr)

    for i in range(mini, maxi+1):
        if isPossible(arr, i, m, k):
            return i
    return -1

class Solution:
    def minDays(self, arr, m, k):
        if len(arr) < m*k:
            return -1
    
        low = min(arr)
        high = max(arr)
        ans = -1

        while low<=high:
            mid = (low + high)//2
            if self.isPossible(arr, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def isPossible(self, arr, day, m, k):
        ans = 0
        count = 0
        for i in arr:
            if i <= day:
                count += 1
            else:
                ans += count//k
                count = 0
        ans += count//k
        return ans >= m
