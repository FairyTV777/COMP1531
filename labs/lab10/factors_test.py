import pytest
from factors import factors, is_prime
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_factor_normal():
    assert list(factors(2)) == [2]
    assert list(factors(6)) == [2,3]
    assert list(factors(9)) == [3,3]
    assert list(factors(12)) == [2,2,3]
    assert list(factors(64)) == [2,2,2,2,2,2]

def test_factor_prime():
    assert list(factors(3)) == [3]
    assert list(factors(5)) == [5]
    assert list(factors(7)) == [7]
    assert list(factors(11)) == [11]

def test_factor_error():
    with pytest.raises(ValueError):
        assert list(factors(-1))
        assert list(factors(0))
        assert list(factors(1))
