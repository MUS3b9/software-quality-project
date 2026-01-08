def login(username, password):
    if not username or not password:
        return "Fields cannot be empty"

    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid credentials"
