n = 3

print(bin(n)[2:])

lsb = n&1

if lsb:
    print('Odd')
else:
    print('Even')