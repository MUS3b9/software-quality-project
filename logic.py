import logic


def test_valid_login(monkeypatch):
    monkeypatch.setattr(
        logic, "load_users",
        lambda: [{"username": "admin", "password": "1234"}]
    )
    assert logic.login("admin", "1234") == "Login successful"


def test_invalid_login(monkeypatch):
    monkeypatch.setattr(
        logic, "load_users",
        lambda: [{"username": "admin", "password": "1234"}]
    )
    assert logic.login("admin", "wrong") == "Invalid credentials"


def test_signup_new_user(monkeypatch):
    users = [{"username": "admin", "password": "1234"}]

    monkeypatch.setattr(logic, "load_users", lambda: users)
    monkeypatch.setattr(logic, "save_users", lambda x: None)

    result = logic.signup("newuser", "1111")
    assert result == "Account created successfully"
