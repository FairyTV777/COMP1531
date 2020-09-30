from prefix import prefix_search

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_str_match():
    assert prefix_search({"comp2521": "data structure", "comp1531": "software engineering", "math1081": "discrete math"}, "comp") \
                            == {"comp2521": "data structure", "comp1531": "software engineering"}

def test_char_match():
    assert prefix_search({"comp2521": "data structure", "comp1531": "software engineering", "math1081": "discrete math"}, "m") \
                            == {"math1081": "discrete math"}