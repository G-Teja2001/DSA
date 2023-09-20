def findXOR(L: int, R: int) -> int:
    def xorTilln(n):
        if n % 4 == 0:
            return n
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        if n % 4 == 3:
            return 0

    xor_left = xorTilln(L - 1)
    xor_right = xorTilln(R)
    ans = xor_left ^ xor_right
    return ans

print(findXOR(3, 5))