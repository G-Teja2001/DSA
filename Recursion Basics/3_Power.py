def fun(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/fun(base, -exponent)
    else:
        return base * fun(base, exponent-1)

print(fun(3, 3))