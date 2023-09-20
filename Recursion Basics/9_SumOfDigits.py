def sum(n, k=0):
    if n<=0:
        return k
    return sum(n//10, k+(n%10))

print(sum(34))