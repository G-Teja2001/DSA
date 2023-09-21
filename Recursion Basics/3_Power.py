def fun(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/fun(base, -exponent)
    else:
        return base * fun(base, exponent-1)

print(fun(3, 3))


# Reduced Recursive Calls..
def optimized_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    if exponent % 2 == 0:
        result = optimized_power(base, exponent // 2)
        return result * result
    else:
        result = optimized_power(base, (exponent - 1) // 2)
        return base * result * result

print(optimized_power(3, 3))
