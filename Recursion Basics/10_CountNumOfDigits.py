def sum(n, k=0):
    if n<=0:
        return k
    return sum(n//10, k+1)

print(sum(33874640))