def fun1(n):
    if n == 0 or n == 1:
        return 1
    return n * fun1(n-1)

print(fun1(6))

def fun2(n, k):
    if n == 0 or n == 1:
        return k
    return fun2(n-1, k*n)

print(fun2(6, 1))