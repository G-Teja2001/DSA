def naive(string, pattern):
    n = len(string)
    m = len(pattern)

    for i in range(n-m+1):
        j = 0
        while j != m:
            if string[i+j] != pattern[j]:
                break
            j += 1
        if j == m:
            print(i, end=' ')

def naive_distinct(string, pattern):
    n = len(string)
    m = len(pattern)

    i = 0
    while i < n-m+1:
        j = 0
        while j != m:
            if string[i+j] != pattern[j]:
                break
            j += 1
        if j == m:
            print(i, end=' ')
        if j == 0:
            i += 1
        else:
            i += j

naive('ABABABCD', 'AB')
print()

naive_distinct('ABABABCD', 'AB')
print()

naive('AAAAA', 'AA')
print()
# This won't work fine.. as the chars aren't distinct.
naive_distinct('AAAAA', 'AA')
