from fibonacci import generate

def test_generate_empty():
    assert generate(0) == []

def test_generate_one():
    assert generate(1) == [0]

def test_generate_normal():
    assert generate(2) == [0, 1]
    assert generate(3) == [0, 1, 1]
    assert generate(10) == [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
