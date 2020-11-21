def divisors(n):
	'''
	Given some number n, return a set of all the numbers that divide it. For example:
	>>> divisors(12)
	{1, 2, 3, 4, 6, 12}
	Params:
		n (int): The operand
	Returns:
		(set of int): All the divisors of n

	Raises:
		ValueError: If n is not a positive integer
	'''
	if n <= 0 or type(n) != int:
		raise ValueError("n should be a positive integer")
	else:
		result = set()
		for i in range(1, n+1):
			if n % i == 0:
				result.add(i)
			i += 1
		return result