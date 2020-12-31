import math


def find_fibonacci_seq_iter(n):
    """
    find a nth term of Fibonacci sequence without recursion O(2^n)
    """
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def find_fibonacci_seq_rec(n):
    """
    find a nth term of Fibonacci sequence with recursion O(n^2)
    """
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)


def find_fibonacci_seq_form(n):
    """
    find a nth term of Fibonacci sequence with formula O(1)
    """
    sqrt_5 = math.sqrt(5)
    phi_1 = (1+sqrt_5)/2
    phi_2 = (1-sqrt_5)/2
    return int((phi_1**n - phi_2**n)/sqrt_5)
