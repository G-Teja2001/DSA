def permute(str, l):
    n = len(str)
    if l == n:
        print(''.join(str), end=' ')
        return
    
    for i in range(l, n):
        str[l], str[i] = str[i], str[l]
        permute(str, l + 1)
        str[l], str[i] = str[i], str[l]

str = list("ABC")
permute(str, 0)
