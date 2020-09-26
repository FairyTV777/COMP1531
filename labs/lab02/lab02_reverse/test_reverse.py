'''
Tests for reverse_words()
'''
from reverse import reverse_words

def test_reverse_words():
    list = []
    assert(reverse_words(list) == [])
    list = ["Hello"]
    assert(reverse_words(list) == ["Hello"])
    list = ["Hello world"]
    assert(reverse_words(list) == ["world Hello"])
    list = ["Hello World", "I am here"]
    assert(reverse_words(list) == ['World Hello', 'here am I'])
    list = ["Hello World", "I am here", "Python is easy"]
    assert(reverse_words(list) == ['World Hello', 'here am I', 'easy is Python'])
