from divisors import divisors
from hypothesis import given, strategies
import pytest

def test_12():
    assert divisors(12) == {1,2,3,4,6,12}

def test_1():
    assert divisors(1) == {1}

def test_2():
    assert divisors(2) == {1,2}

def test_9():
    assert divisors(9) == {1,3,9}

def test_0():
    with pytest.raises(ValueError):
        assert divisors(0)

def test_negative():
    with pytest.raises(ValueError):
        assert divisors(-1)

def test_not_int():
    with pytest.raises(ValueError):
        assert divisors(0.1)
