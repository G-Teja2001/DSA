def elementThatAppearsOnce(arr):
    result = 0
    for i in range(32):
        count = 0
        for num in arr:
            # Count the number of elements with the current bit set
            if (num >> i) & 1:
                count += 1

        # If the count is not a multiple of 3, it's a bit of the single number
        if count % 3 != 0:
            # Set the bit in the result
            result |= (1 << i)

    return result