from weather import weather

def test_weather_normal():
    assert weather('08-08-2010', 'Albury') == (10.8, 10.0)
    assert weather('08-06-2017', 'Sydney') == (2.5, 4.9)

def test_weather_empty():
    assert weather('   ', '    ') == (None, None)
    assert weather('    ', 'Sydney') == (None, None)
    assert weather('08-08-2010', '   ') == (None, None)

def test_weather_invalid():
    assert weather('30-09-2020', 'Sydney') == (None, None)
    assert weather('08-06-2017', 'Wuhan') == (None, None)