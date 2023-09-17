n = 3

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in reversed(range(i+1)):
        print(j+1, end='')
    for j in reversed(range(1, i+1)):
        print(j+1, end='')
    print()