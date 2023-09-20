def fun(n):
    if n == 0:
        return 0
    print(n%2, end='')
    fun(int(n/2))

print(fun(0))