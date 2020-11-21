def permutations(string):
	'''
	For the given string, compute the set of all permutations of the characters of that string. For example:
	>>> permutations('ABC')
	{'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

	Params:
	  	string (str): The string to permute

	Returns:
	  	(set of str): Each string in this set should be a permutation of the input string.
	'''
	if string == "":
		return {""}
	result = set()
	for i in range(len(string)):
		before = string[:i]
		after = string[i+1:]
		for rest in permutations(before + after):
			result.add(string[i]+rest)
	return result
		