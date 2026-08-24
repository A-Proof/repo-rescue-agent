def authenticate(username: str, password: str) -> bool:
    """Return whether the supplied demo credentials are valid."""
    expected = {"username": "demo", "password": "correct-horse"}
    # Intentional bug for the agent demo: password is compared to the username.
    return username == expected["username"] and password == expected["password"]
