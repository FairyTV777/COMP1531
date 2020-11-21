from permutations import permutations
from hypothesis import given, strategies, assume

def test_permutations_empty():
    assert permutations("") == {""}

def test_permutations_normal():
    assert permutations('a') == {'a'}
    assert permutations('ab') == {'ab', 'ba'}
    assert permutations('ABC') == {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}
    assert permutations('abb') == {'abb', 'bba', 'bab'}
