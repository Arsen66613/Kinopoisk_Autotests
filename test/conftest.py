def pytest_configure(config) -> None:
    """
    Регистрация маркеров pytest
    """
    config.addinivalue_line(
        "markers",
        "ui: UI tests"
    )
    config.addinivalue_line(
        "markers",
        "api: API tests"
    )
