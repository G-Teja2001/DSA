def generate_permutations(arr):
    permutations = []
    n = len(arr)
    
    # Generate all permutations using a recursive function
    def generate_helper(arr, start):
        if start == n - 1:
            permutations.append(arr.copy())
        else:
            for i in range(start, n):
                arr[start], arr[i] = arr[i], arr[start]  # Swap elements
                generate_helper(arr, start + 1)           # Recursively generate permutations
                arr[start], arr[i] = arr[i], arr[start]  # Swap back to backtrack
                
    generate_helper(arr, 0)
    return permutations

def find_next_permutation(arr):
    permutations = generate_permutations(arr)
    n = len(arr)
    # Linear search
    for i in range(len(permutations)):
        if permutations[i] == arr:
            if i == len(permutations) - 1:
                return permutations[0]  # If it's the last permutation, return the first
            else:
                return permutations[i + 1]  # Return the next permutation
    
    return arr  # If the current permutation is not found (shouldn't happen)

# Example usage:
arr = [4, 3, 2, 1]
next_permutation = find_next_permutation(arr)
print(next_permutation)
