def countDistinctBitwiseOR(arr, size):
    distinct_bitwise_or = set()
    current_bits = set()

    for num in arr:
        new_bits = set()
        new_bits.add(num)

        for bits in current_bits:
            new_bits.add(bits | num)

        current_bits = new_bits
        distinct_bitwise_or.update(current_bits)

    return len(distinct_bitwise_or)