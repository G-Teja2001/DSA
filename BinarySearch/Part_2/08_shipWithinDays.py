from typing import List

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Define a helper function to check if a given capacity is feasible
        def is_feasible(capacity):
            days_needed = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= capacity:
                    current_weight += weight
                else:
                    days_needed += 1
                    current_weight = weight

            return days_needed <= D

        # Start the loop from the maximum weight and check each capacity
        max_weight = max(weights)
        for capacity in range(max_weight, sum(weights) + 1):
            if is_feasible(capacity):
                return capacity

# Example usage:
solution = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
result = solution.shipWithinDays(weights, D)
print(result)  # Output: 15








# The only diff is that we have a diff range thats it 

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Define the search range
        low = max(weights)  # Minimum capacity can't be less than the weight of the heaviest item
        high = sum(weights)  # Maximum capacity can't be more than the total weight

        while low < high:
            mid = (low + high) // 2
            if self.isPossible(weights, D, mid):
                high = mid
            else:
                low = mid + 1

        return low

    def isPossible(self, weights, D, capacity):
        days_needed = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight <= capacity:
                current_weight += weight
            else:
                days_needed += 1
                current_weight = weight

        return days_needed <= D

# Example usage:
solution = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
result = solution.shipWithinDays(weights, D)
print(result)  # Output: 15
