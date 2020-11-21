from inverse import inverse
from hypothesis import given, strategies

def test_inverse_empty():
    assert inverse({}) == {}

def test_inverse_normal():
    assert inverse({1: 'A', 2: 'A'}) == {'A': [1,2]}
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}
    assert inverse({1: 'A', 2: 'B', 3: 'A', 4: 'B'}) == {'A': [1,3], 'B': [2,4]}