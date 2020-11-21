from balanced import balanced
from hypothesis import given, strategies

def test_balanced():
    assert balanced(6) == {'((()))', '(()())', '(())()', '()(())', '()()()'}
