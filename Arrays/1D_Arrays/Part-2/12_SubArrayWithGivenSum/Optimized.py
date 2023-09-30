def subarraySum(self, nums, k):
    sum_frequency = {}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        # If the current sum is equal to k, increment the count
        if current_sum == k:
            count += 1

        # If the current sum - k has been seen before, add its frequency to the count
        if current_sum - k in sum_frequency:
            count += sum_frequency[current_sum - k]

        # Increment the frequency of the current sum
        if current_sum in sum_frequency:
            sum_frequency[current_sum] += 1
        else:
            sum_frequency[current_sum] = 1

    return count