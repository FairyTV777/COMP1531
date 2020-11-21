def balanced(n):
	'''
	Given a positive number n, compute the set of all strings of length n, in any order, that only
	contain balanced brackets. For example:
	>>> balanced(6)
	{'((()))', '(()())', '(())()', '()(())', '()()()'}
	Note that, by definition, the only string of length 0 containing balanced brackets is the empty
	string.
	Params:
		n (int): The length of string we want
	Returns:
		(set of str): Each string in this set contains balanced brackets. In the event n is odd, this
		set is empty.

	Raises:
		ValueError: If n is negative
	'''
	if type(n) != int or n < 0:
		raise ValueError("n should not be negative.")
	
	if n == 0:
		return {''}
	
	if n % 2 == 1:
		return set()

	result = set()
	for i in range(2,n,2):
		for j in balanced(i):
			for k in balanced_unit(n-i):
				result.add(j+k)

	result.update(balanced_unit(n))
	return result

def balanced_unit(n):
	if n == 2:
		return {"()"}

	result = set()
	for a in balanced(n-2):
		result.add("(" + a + ")")
	return result
	