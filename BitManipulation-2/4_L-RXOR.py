def xorTilln(n):
    if n%4 == 0:
        return(n)
    if n%4 == 1:
        return(1)
    if n%4 == 2:
        return(n+1)
    if n%4 == 3:
        return(0)

left = xorTilln(int(input('Enter a num: ')))
right = xorTilln(int(input('Enter a num: ')))

ans = left ^ right
print(ans)