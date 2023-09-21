# O(N!)
def permute(str, l, r):
    if l == r:
        print(''.join(str), end=' ')
    else:
        for i in range(l, r + 1):
            str[l], str[i] = str[i], str[l]  # Swap characters
            permute(str, l + 1, r)  # Recursively generate permutations
            str[l], str[i] = str[i], str[l]  # Backtrack to the original string

str = list("ABC")
permute(str, 0, len(str) - 1)
