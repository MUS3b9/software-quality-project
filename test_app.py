from app import login, signup

def test_valid_login():
    assert login("admin", "1234") == "Login successful"

def test_invalid_login():
    assert login("admin", "wrong") == "Invalid credentials"

def test_empty_fields_login():
    assert login("", "") == "Fields cannot be empty"

def test_signup_new_user():
    result = signup("newuser", "1111")
    assert result == "Account created successfully"

def test_signup_existing_user():
    result = signup("admin", "1234")
    assert result == "User already exists"
