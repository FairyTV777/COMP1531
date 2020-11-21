'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
	return n != 1 and divisors(n) == {1, n}

def factors(n):
	'''
	A generator that generates the prime factors of n. For example
	>>> list(factors(12))
	[2,2,3]

	Params:
	  	n (int): The operand

	Yields:
	  	(int): All the prime factors of n in ascending order.

	Raises:
	  	ValueError: When n is <= 1.
	'''
	if n <= 1:
		raise ValueError(f"{n} does not have prime factors.")
	for divisor in sorted(divisors(n)):
		if is_prime(divisor):
			while n != 1 and n % divisor == 0:
				yield divisor
				n = n/divisor