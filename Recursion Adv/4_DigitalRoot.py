def digitalRoot(n):
    # Base case: If n is a single-digit number, return n
    if n < 10:
        return n
    
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    
    # Recursively call digitalRoot on the sum
    return digitalRoot(digit_sum)

print(digitalRoot(1002))
print(digitalRoot(99999))
