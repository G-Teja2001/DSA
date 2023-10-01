def reverseWords(string):
    n = len(string)
    # Strings are immutable -> We cant assign them directly by accessing their index.
    string = list(string)

    start = 0
    for end in range(n):
        if string[end] == ' ':
            reverse(string, start, end-1)
            start = end + 1

    reverse(string, start, n-1)
    reverse(string, 0, n-1)

    return ''.join(string)

def reverse(string, left, right):
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1

print(reverseWords('Welcome to Gfg'))