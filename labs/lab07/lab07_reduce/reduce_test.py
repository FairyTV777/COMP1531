from reduce import reduce

def test_reduce_empty():
   assert reduce(lambda x, y: x + y, []) == None
   assert reduce(lambda x, y: x * y, []) == None
   assert reduce(lambda x, y: x + y, '') == None

def test_reduce_one():
   assert reduce(lambda x, y: x + y, [1]) == 1
   assert reduce(lambda x, y: x * y, [1]) == 1
   assert reduce(lambda x, y: x + y, 'a') == 'a'

def test_reduce_normal():
   assert reduce(lambda x, y: x + y, [1,2,3,4,5]) == 15
   assert reduce(lambda x, y: x * y, [1,2,3,4,5]) == 120
   assert reduce(lambda x, y: x + y, 'abcdefg') == 'abcdefg'
