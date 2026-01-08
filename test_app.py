from app import login

def test_valid_login():
    assert login("admin", "1234") == "Login successful"

def test_invalid_login():
    assert login("admin", "wrong") == "Invalid credentials"

def test_empty_fields():
    assert login("", "") == "Fields cannot be empty"
