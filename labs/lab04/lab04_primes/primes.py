import math

def factors(num):
    '''
    Returns a list containing the prime factors of 'num'. The primes should be
    listed in ascending order.

    For example:
    >>> factors(16)
    [2, 2, 2, 2]
    >>> factors(21)
    [3, 7]
    '''
    factors = []
    quotient = num
    i = 2
    while i <= num and quotient != 1:
        while quotient % i == 0 and quotient != 1:
            quotient = quotient / i
            factors.append(i)
        i += 1

    return factors
