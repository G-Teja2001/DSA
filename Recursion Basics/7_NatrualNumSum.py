def fun(n):
    if n<1:
        return n
    return n + fun(n-1)

print(fun(5))

def fun2(n, k):
    if n<1:
        return k
    return fun2(n-1, n+k)

print(fun2(5, 0))