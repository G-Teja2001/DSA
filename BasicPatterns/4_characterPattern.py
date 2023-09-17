n = 4

char = 'a'

for i in range(n):
    for j in range(i + 1):
        print(char, end='')
        char = chr(ord(char) + 1)
    print()
