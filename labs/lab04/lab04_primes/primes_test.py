from primes import factors

def test_factors():
    assert factors(16) == [2, 2, 2, 2]
    assert factors(21) == [3, 7]
    assert factors(1) == []
    assert factors(1014) == [2, 3, 13, 13]
    assert factors(540) == [2, 2, 3, 3, 3, 5]