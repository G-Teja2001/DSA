def fun(n, k):
    if n%k == 0:
        return False
    
    if n<k:
        return True
    
    return fun(n-n//2, k+1)

print(fun(5, 2))