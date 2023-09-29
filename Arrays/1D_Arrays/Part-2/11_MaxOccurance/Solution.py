from collections import OrderedDict


arr1 = [1, 2, 5, 15]
arr2 = [5, 8, 7, 18]

def naive(arr1, arr2):
    hashTable = OrderedDict()

    for i in range(len(arr1)):
        elem1 = arr1[i]
        elem2 = arr2[i]
        for j in range(elem1, elem2+1):
            if hashTable.get(j):
                hashTable[j] += 1
            else:
                hashTable[j] = 1
    
    max_occurrence = 0
    max_number = None
    for num, count in hashTable.items():
        if count > max_occurrence:
            max_occurrence = count
            max_number = num

    return max_number, max_occurrence


def optimized(arr1, arr2):
    max_range = max(max(arr2), max(arr1))
    diff_array = [0] * (max_range + 1)
    
    for i in range(len(arr1)):
        elem1 = arr1[i]
        elem2 = arr2[i]
        diff_array[elem1] += 1
        if elem2 + 1 <= max_range:
            diff_array[elem2 + 1] -= 1
    
    # Prefix sum
    max_occurrence = -1
    max_number = None
    current_sum = 0
    for i in range(max_range + 1):
        current_sum += diff_array[i]
        if current_sum > max_occurrence:
            max_occurrence = current_sum
            max_number = i

    return max_number, max_occurrence

print(optimized(arr1, arr2))

