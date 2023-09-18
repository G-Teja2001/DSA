a = 3
n = 5

ans = 1

while n>0:
    if n & 1:
        ans = ans * a
    a = a * a
    n = n >> 1

print(ans)