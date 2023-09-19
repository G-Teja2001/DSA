def generate_power_set(input_set):
    n = len(input_set)
    power_set = []

    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(input_set[j])
        power_set.append(subset)

    return power_set

input_set = [1, 2, 3]
result = generate_power_set(input_set)
print(result)
