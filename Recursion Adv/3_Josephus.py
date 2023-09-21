def fun(n, k):
    if n == 1:
        return 0
    
    return (fun(n-1, k) + k) % n

print(fun(7, 3))