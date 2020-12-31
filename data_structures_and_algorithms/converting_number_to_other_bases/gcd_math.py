def finding_gcd(a, b):
    """
    greater common divisor
    """
    result = 0
    while b != 0:
        result = b
        a, b = b, a % b
    return result


a = finding_gcd(12, 21)
print(a)
