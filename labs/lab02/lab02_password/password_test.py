'''
Tests for check_password()
'''
from password import check_password

def test_check_password():
    password = "password"
    assert(check_password(password) == "Horrible password")
    password = "1234567890AbCdef"
    assert(check_password(password) == "Strong password")
    password = "12345678"
    assert(check_password(password) == "Moderate password")
    password = "123"
    assert(check_password(password) == "Poor password")
    password = "123456"
    assert(check_password(password) == "Horrible password")