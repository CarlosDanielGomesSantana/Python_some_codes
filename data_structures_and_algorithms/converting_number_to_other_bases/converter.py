"""
todo: try to implement using OO
todo: make a better implemantations with handle errors and conditions
"""


def convert_to_decimal(number, base):
    """
    convert a number in base 2 < base < 10 to decimal
    """
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10*multiplier
        multiplier *= base
        number //= 10
    return result


def convert_from_decimal(number, base):
    """
    convert a decimal to 2 < base < 10
    """
    multiplier, result = 1, 0
    while number > 0:
        result += number % base*multiplier
        multiplier *= 10
        number //= base
    return result


def convert_from_decimal_larger_bases(number, base):
    """
    convert a decimal to 2 < base < 20
    """
    algarithms = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = algarithms[digit] + result
        number //= base
    return result


def convert_dec_to_any_base_rec(number, base):
    algarithms = "0123456789ABCDEF"
    if number < base: return algarithms[number]
    else: return convert_dec_to_any_base_rec(number//base, base) + algarithms[number % base]

