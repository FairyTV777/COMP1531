from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_long():
    assert count_char("abcdefgh") == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g":1, "h": 1}

def test_complex():
    assert count_char("ab13cd34") == {"a": 1, "b": 1, "c": 1, "d": 1, "1": 1, "3": 2, "4": 1}

def test_more_complex():
    assert count_char("HelloOo!") == {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'O': 1, '!': 1}