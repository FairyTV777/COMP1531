from list_exercises import *

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]
    reverse_list(l)
    assert l == ["how", "are", "you"]
    l.append("?")
    reverse_list(l)
    assert l == ["?", "you", "are", "how"]

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1
    assert minimum([-2, 1, 2, 3, 10]) == -2
    assert minimum([1, 1]) == 1

def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([-1, -2, -3]) == -6
    assert sum_list([0, 0, 0]) == 0