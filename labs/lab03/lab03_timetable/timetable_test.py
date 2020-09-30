""" 
Tests for timetable()
"""
from timetable import timetable
from datetime import date, time, datetime

def test_timetable():
    assert timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)]) \
            == [datetime(2019, 9, 27, 10, 30), datetime(2019, 9, 27, 14, 10), datetime(2019, 9, 30, 10, 30), datetime(2019, 9, 30, 14, 10)]

    assert timetable([], []) == []

    assert timetable([date(2018,10,11)], [time(14,41)]) == [datetime(2018, 10, 11, 14, 41)]

    assert timetable([date(2019,5,16), date(2019,9,10)], [time(7,44)]) == [datetime(2019, 5, 16, 7,44), datetime(2019, 9, 10, 7, 44)]